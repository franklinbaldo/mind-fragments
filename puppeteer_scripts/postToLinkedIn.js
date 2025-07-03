const puppeteer = require('puppeteer');

async function postToLinkedIn(username, password, postContent, options = {}) {
  let browser = null;
  try {
    console.log('Launching browser...');
    // Default options for Puppeteer launch
    const launchOptions = {
      headless: options.headless !== undefined ? options.headless : true, // Default to true (headless)
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage', // Recommended for Docker
        '--disable-accelerated-2d-canvas',
        '--no-first-run',
        '--no-zygote',
        // '--single-process', // Not recommended for general use, but can help in resource-constrained environments
        '--disable-gpu'
      ]
    };

    // If running inside Docker with the puppeteer_runner service,
    // Chrome should be found automatically by Puppeteer.
    // If connecting to a remote browser (e.g. browserless/chrome), you'd use puppeteer.connect here.
    browser = await puppeteer.launch(launchOptions);
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 800 });

    console.log('Navigating to LinkedIn login page...');
    await page.goto('https://www.linkedin.com/login', { waitUntil: 'networkidle2' });

    console.log('Typing username...');
    await page.type('#username', username);
    console.log('Typing password...');
    await page.type('#password', password);

    console.log('Clicking login button...');
    await page.click('.login__form_action_container button[type="submit"]');

    // Wait for navigation after login. This could be to the feed or a security check.
    // It's crucial to have robust waiting strategies.
    console.log('Waiting for navigation to feed after login...');
    try {
      await page.waitForSelector('input[placeholder="Search"]', { timeout: 30000 }); // Wait for search bar on feed
      console.log('Successfully logged in and feed loaded.');
    } catch (e) {
      console.error('Failed to verify login or load feed. Page content:', await page.content());
      // You might be on a security check page or something else.
      // Add handling for security checks (e.g., CAPTCHA, 2FA) if necessary.
      // For now, we'll throw an error if the feed isn't detected.
      await page.screenshot({ path: '/usr/src/app/scripts/linkedin_login_error.png' });
      throw new Error('LinkedIn login failed or feed did not load as expected.');
    }

    console.log('Clicking on "Start a post" button/area...');
    // LinkedIn's UI changes. This selector is a common one but might need updates.
    // const startPostSelector = 'button.artdeco-button--primary.share-unified-settings-entry-button'; // More specific
    const startPostSelectorArea = '.share-box-feed-entry__trigger'; // Clickable area
    try {
        await page.waitForSelector(startPostSelectorArea, { timeout: 10000 });
        await page.click(startPostSelectorArea);
    } catch(e) {
        console.error("Could not find 'Start a post' button/area. Trying alternative selector.");
        // Fallback or more general selector if the primary one fails
        // This often happens due to A/B testing or UI updates by LinkedIn.
        // It might be a button with text "Start a post"
        const altStartPostSelector = 'button[aria-label="Start a post"]'; // Common for accessibility
         try {
            await page.waitForSelector(altStartPostSelector, { timeout: 10000 });
            await page.click(altStartPostSelector);
        } catch (e2) {
            console.error("Alternative 'Start a post' selector also failed.");
            await page.screenshot({ path: '/usr/src/app/scripts/linkedin_start_post_error.png' });
            throw new Error("Could not find 'Start a post' button or area.");
        }
    }


    console.log('Waiting for post modal to appear...');
    // The modal editor usually has a specific class or role.
    const postEditorSelector = '.ql-editor'; // The actual text input area
    const postButtonSelector = 'button.share-actions__primary-action'; // The "Post" button

    await page.waitForSelector(postEditorSelector, { timeout: 10000 });
    console.log('Typing post content...');
    await page.type(postEditorSelector, postContent);

    // Wait a bit for the post button to become enabled if necessary
    await page.waitForTimeout(1000);

    console.log('Clicking post button...');
    await page.waitForSelector(postButtonSelector, { visible: true, timeout:10000 });
    await page.click(postButtonSelector);

    console.log('Waiting for post confirmation (e.g., modal closes or success message)...');
    // This is tricky. A common way is to wait for the modal to disappear.
    // Or look for a "Post successful" message.
    // For now, let's assume the modal closes. We can wait for the editor to be hidden.
    await page.waitForFunction(
        (selector) => !document.querySelector(selector),
        { timeout: 20000 },
        postEditorSelector
    );

    console.log('Post successful!');
    await page.screenshot({ path: '/usr/src/app/scripts/linkedin_post_success.png' });

  } catch (error) {
    console.error('Error during LinkedIn Puppeteer script:', error);
    if (page) {
        await page.screenshot({ path: '/usr/src/app/scripts/linkedin_error_screenshot.png' });
        console.log('Error screenshot saved to linkedin_error_screenshot.png');
    }
    throw error; // Re-throw the error to be caught by N8N or the calling script
  } finally {
    if (browser) {
      console.log('Closing browser...');
      await browser.close();
    }
  }
}

// --- Main execution ---
// This part is for running the script directly using `node postToLinkedIn.js username password "My post content"`
// N8N's Execute Command node will pass arguments like this.
if (require.main === module) {
  const args = process.argv.slice(2); // First two are node and script path
  if (args.length < 3) {
    console.error('Usage: node postToLinkedIn.js <username> <password> <postContent> [--no-headless]');
    process.exit(1);
  }
  const username = args[0];
  const password = args[1];
  const postContent = args[2];
  const options = {
    headless: !args.includes('--no-headless') // Set headless to false if --no-headless is present
  };

  postToLinkedIn(username, password, postContent, options)
    .then(() => console.log('LinkedIn script finished successfully.'))
    .catch(err => {
        console.error('LinkedIn script failed:', err);
        process.exit(1);
    });
}

module.exports = postToLinkedIn; // Export for potential programmatic use (though less likely with N8N Execute Command)
