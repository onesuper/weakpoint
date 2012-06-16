/*
 * weakpoint.js
 * (c) 2012 onesuper
 */

allSlides = document.querySelectorAll('section');
addEventListeners();   
currentSlide = 0;
goSlide(0);


function addEventListeners() {
    document.addEventListener('keydown', onKeyDown, false);
    document.addEventListener('mousedown', onMouseDown, false);
}

function onKeyDown(event) {
    switch(event.keyCode) {
    case 33: case 37: previousSlide();break;
    case 34: case 39: nextSlide();break;    
    case 36: goSlide(0);break;
    }
}

function onMouseDown(event) {
    switch(event.which) {
    case 1: nextSlide();break; 
    }
}

function hideAll() {
    var allLists = document.querySelectorAll('li');
    for (var i=0; i<allLists.length; i++) {
	allLists[i].style.display ="none";
    }
    var allP = document.querySelectorAll('p');
    for (var i = 0; i < allP.length; i++) {
	allP[i].style.display = "none";
    }
}

function previousSlide() {
    if (currentSlide ==0)
	return

    var allLists = allSlides[currentSlide].querySelectorAll('li');
    for (var i = allLists.length - 1; i >= 0; i--) {
	if (allLists[i].style.display == "list-item") {
	    allLists[i].style.display = "none";
	    return;
	}
    }

    var allP = allSlides[currentSlide].querySelectorAll('p');
    for (var i = allP.length - 1; i >= 0; i--) {
	if (allP[i].style.display == "block") {
	    allP[i].style.display = "none";
	    return;
	}
    }

    allSlides[currentSlide].style.display = "none";
    allSlides[currentSlide-1].style.display = "block";
    currentSlide -= 1;
}

function nextSlide() {
    if (currentSlide == allSlides.length - 1)
	return

    var allLists = allSlides[currentSlide].querySelectorAll('li');
    for (var i = 0; i < allLists.length; i++) {
	if (allLists[i].style.display == "none") {
	    allLists[i].style.display = "list-item";
	    return;
	}
    }

    var allP = allSlides[currentSlide].querySelectorAll('p');
    for (var i = 0; i < allP.length; i++) {
	if (allP[i].style.display == "none") {
	    allP[i].style.display = "block";
	    return;
	}
    }

    allSlides[currentSlide].style.display = "none";
    allSlides[currentSlide+1].style.display = "block";
    currentSlide += 1;
}

function goSlide(i) {
    allSlides[currentSlide].style.display = "none";
    allSlides[i].style.display = "block";
    currentSlide = i;
    hideAll();
}
    