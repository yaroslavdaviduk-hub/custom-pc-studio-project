document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.querySelector('.navbar');
  const trigger = document.getElementById('menuHover');
  const collapseEl = document.getElementById('hoverCollapse');

  // высота navbar
  const setNavbarHeight = () => {
    document.documentElement.style.setProperty(
      '--navbar-height',
      `${navbar.offsetHeight}px`
    );
  };

  setNavbarHeight();
  window.addEventListener('resize', setNavbarHeight);

  const collapse = new bootstrap.Collapse(collapseEl, { toggle: false });
  let isOpen = false;

  const openMenu = () => {
    if (!isOpen) {
      collapse.show();
      document.body.classList.add('menu-open');
      isOpen = true;
    }
  };

  const closeMenu = () => {
    if (isOpen) {
      collapse.hide();
      document.body.classList.remove('menu-open');
      isOpen = false;
    }
  };

  trigger.addEventListener('mouseenter', openMenu);
  collapseEl.addEventListener('mouseenter', openMenu);

  trigger.addEventListener('mouseleave', () => {
    setTimeout(() => {
      if (!collapseEl.matches(':hover')) closeMenu();
    }, 120);
  });

  collapseEl.addEventListener('mouseleave', closeMenu);
});
