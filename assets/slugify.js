const titleInpute = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-')
    .replace(/[\s\W-]+/g,'-')
};

titleInpute.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value',slugify(titleInpute.value));

});