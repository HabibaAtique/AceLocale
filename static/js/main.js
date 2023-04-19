const socialLinks = [
  { platform: 'Facebook', url: 'https://www.facebook.com/', icon: 'fab fa-facebook' },
  { platform: 'Twitter', url: 'https://twitter.com/', icon: 'fab fa-twitter' },
  { platform: 'Instagram', url: 'https://www.instagram.com/', icon: 'fab fa-instagram' },
  { platform: 'LinkedIn', url: 'https://linkedin.com/', icon: 'fab fa-linkedin' },
  { platform: 'Youtube', url: 'https://www.youtube.com/', icon: 'fab fa-youtube' },
];

const socialIcons = document.querySelector('.social ul');

socialLinks.forEach(link => {
  const icon = document.createElement('i');
  icon.className = link.icon;

  const anchor = document.createElement('a');
  anchor.href = link.url;
  anchor.appendChild(icon);

  const listItem = document.createElement('li');
  listItem.appendChild(anchor);

  socialIcons.appendChild(listItem);
});
