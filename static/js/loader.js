function loadPage(url) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.innerHTML = xhr.responseText;
            history.pushState(null, '', url);
        }
    };
    xhr.send();
}

function sendForm(url, method, form=null) {
    const xhr = new XMLHttpRequest();
    xhr.open(method, url, true);

    let data = null;
    if (form) {
        data = serializeForm(form);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    }

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.innerHTML = xhr.responseText;
            history.pushState(null, '', url);
        }
    };

    xhr.send(data);
}

window.onpopstate = function(event) {
    loadPage(location.href);
};