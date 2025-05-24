document.addEventListener('DOMContentLoaded', async () => {
    async function queryEntry() {
        const observer = new MutationObserver((mutations) => {
            let submit = document.querySelector('button.inline-flex[aria-label="Send message"]');
            console.log('Button:', submit);

            if (submit && !submit.disabled) {
                submit.click();
                observer.disconnect(); // Stop observing once the button is found and clicked
            } else {
                console.log('Button not found or is disabled');
            }
        });

        observer.observe(document.body, { childList: true, subtree: true });
        // Optionally, you can set a timeout to stop observing after a certain period
        setTimeout(() => {
            observer.disconnect();
            console.log('Stopped observing for button');
        }, 500); // Stop observing after 10 seconds
    }

    console.log('Script loaded');
    queryEntry();
});



document.addEventListener('DOMContentLoaded', () => {
    const NEW_PROMPT = '>>> aquí tu texto nuevo <<<';

    if (!setPrompt(NEW_PROMPT)) return;      // Abort if no input

    const observer = new MutationObserver(() => {
        const btn = document.querySelector(
            'button.inline-flex[aria-label="Send message"]'
        );
        if (btn && !btn.disabled) {
            btn.click();
            observer.disconnect();
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
    setTimeout(() => observer.disconnect(), 10_000); // 10 s máx.
});

