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
        }, 10000); // Stop observing after 10 seconds
    }

    console.log('Script loaded');
    queryEntry();
});


//this dont work well beacause only insert the last promp but not the actual