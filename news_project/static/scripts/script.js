let offset = 6;
const limit = 3;
const contentContainer = document.getElementById('content-container');
const loading = document.getElementById('spinner');
let isLoading = false;

console.log('offset: ', offset, 'limit: ', limit);

var myFunction = function(e) {
    if ((window.innerHeight + window.scrollY) >= contentContainer.offsetHeight && !isLoading) {
        isLoading = true;
        loading.style.display = 'block';
        loadMoreContent();
    }
};

window.addEventListener('scroll', myFunction, false);

function loadMoreContent() {
    let tag = window.location.pathname.split('/')[2];
    let url = tag
        ? `/api/news/load_more?offset=${offset}&limit=${limit}` + `&tag=${tag}`
        : `/api/news/load_more?offset=${offset}&limit=${limit}`
    offset += limit;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            isLoading = false;
            loading.style.display = 'none';
            if (data.length === 0) {
                window.removeEventListener('scroll', myFunction, false);
            }
            data.forEach(news => {
            const newsElement = createNewsElementMy(news);
            contentContainer.appendChild(newsElement);
        });
    });
}

function createNewsElementMy(post) {
    // Создания col-4 div
    const colCardElement = document.createElement('div');
    colCardElement.classList.add('col-4');

    // Создание card div
    const cardElement = document.createElement('div');
    cardElement.classList.add('card', 'mb-3');

    // Создание img
    const imgElement = document.createElement('img');
    imgElement.classList.add('card-img-top');
    imgElement.src = post.image;
    imgElement.alt = 'image';

    // Создание card-body div
    const bodyElement = document.createElement('div');
    bodyElement.classList.add('card-body');

    // Создание card-title h5
    const titleElement = document.createElement('h5');
    titleElement.classList.add('card-title');

    // Создание ссылки на новость
    const linkTitleElement = document.createElement('a');
    linkTitleElement.href = `/news/${post.id}`;
    linkTitleElement.textContent = post.title;
    titleElement.appendChild(linkTitleElement);

    // Создание div с тегами
    const tagsElement = document.createElement('div');
    tagsElement.style = "display:flex; gap:5px;";

    // Создание ссылок на теги
    for (let i=0; i<post.tags.length; i++) {
        const linkTag = document.createElement('a');
        linkTag.classList.add('badge', 'text-bg-info', 'text-white');
        linkTag.href = `/tag/${post.tags[i]}`;
        linkTag.textContent = `#${post.tags[i]}`;
        tagsElement.appendChild(linkTag);
    }

    bodyElement.appendChild(titleElement);
    bodyElement.appendChild(tagsElement);
    cardElement.appendChild(imgElement);
    cardElement.appendChild(bodyElement);
    colCardElement.appendChild(cardElement);

    return colCardElement;
}