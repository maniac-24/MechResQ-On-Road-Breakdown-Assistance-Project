document.addEventListener('DOMContentLoaded', () => {
    const htmlElement = document.documentElement;
    const lightModeRadio = document.getElementById('lightModeRadio');
    const darkModeRadio = document.getElementById('darkModeRadio');

    // Function to set the theme
    function setTheme(theme) {
        htmlElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        if (lightModeRadio && darkModeRadio) {
            lightModeRadio.checked = (theme === 'light');
            darkModeRadio.checked = (theme === 'dark');
        }
    }

    // Initialize theme on load
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        setTheme(savedTheme);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        setTheme('dark');
    } else {
        setTheme('light');
    }

    // Add event listeners for radio buttons
    if (lightModeRadio) {
        lightModeRadio.addEventListener('change', () => {
            if (lightModeRadio.checked) {
                setTheme('light');
            }
        });
    }

    if (darkModeRadio) {
        darkModeRadio.addEventListener('change', () => {
            if (darkModeRadio.checked) {
                setTheme('dark');
            }
        });
    }
});
