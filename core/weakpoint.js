/*
 * weakpoint.js
 * (c) 2012 onesuper
 */

addEventListeners();   
goPage(0);
currentPage = 0;

function addEventListeners() {
    document.addEventListener('keydown', onDocumentKeyDown, false);
}

function onDocumentKeyDown(event) {
    switch(event.keyCode) {
    case 33: case 37: previousPage();break;
    case 34: case 39: nextPage();break;    
    }
}

function previousPage() {
    if (currentPage ==0)
	return
    var allPages = document.querySelectorAll('section');
    allPages[currentPage].style.display = "none";
    allPages[currentPage-1].style.display = "inline";
    currentPage -= 1;
}

function nextPage() {
    var allPages = document.querySelectorAll('section');
    if (currentPage == allPages.length - 1)
	return
    allPages[currentPage].style.display = "none";
    allPages[currentPage+1].style.display = "inline";
    currentPage += 1;
}

function goPage(i) {
    var allPages = document.querySelectorAll('section');
    allPages[i].style.display = "inline";
    currentPage = i;
}
    