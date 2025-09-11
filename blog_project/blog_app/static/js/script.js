const toggleBtn = document.getElementById('theme-toggle');
  const body = document.body;

  // Load user preference from localStorage
  if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-mode');
    toggleBtn.textContent = '☀️ Light Mode';
  }

  toggleBtn.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    if (body.classList.contains('dark-mode')) {
      localStorage.setItem('theme', 'dark');
      toggleBtn.textContent = '☀️ Light Mode';
    } else {
      localStorage.setItem('theme', 'light');
      toggleBtn.textContent = '🌙 Dark Mode';
    }
  });