/*
 * weakpoint.js
 * (c) 2012 onesuper
 */

allSlides = document.querySelectorAll('section');
navi = document.getElementsByClassName('navi')[0]
addEventListeners();   
currentSlide = 0;
currentChapter = -1;
goToFirst();


function addEventListeners() {
    document.addEventListener('keydown', onKeyDown, false);
    document.addEventListener('mousedown', onMouseDown, false);
}

function onKeyDown(event) {
    switch(event.keyCode) {
    case 33: case 37: previousSlide();break;
    case 34: case 39: nextSlide();break;    
    case 36: goToFirst();break;
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
    // start
    if (currentSlide ==0)
	return

    //set current chapter
    var h1_list = allSlides[currentSlide].querySelectorAll('h1');
    if (h1_list[0]){	
	currentChapter -= 1;
	//alert(currentChapter);
    }

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
    allSlides[currentSlide].className ="noncurrent";
    allSlides[currentSlide-1].style.display = "block";
    allSlides[currentSlide-1].className = "current";
    currentSlide -= 1;
    processNavi();
}

function nextSlide() {
    // end
    if (currentSlide == allSlides.length - 1)
	return

    //set current chapter
    var h1_list = allSlides[currentSlide].querySelectorAll('h1');
    if (h1_list[0]) {
	currentChapter += 1;
	//alert(currentChapter);
    }

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
    allSlides[currentSlide].className = "noncurrent";
    allSlides[currentSlide+1].style.display = "block";
    allSlides[currentSlide+1].className = "current";
    currentSlide += 1;
    processNavi();


}

function goToFirst() {
    allSlides[currentSlide].style.display = "none";
    allSlides[currentSlide].className = "noncurrent";
    allSlides[0].style.display = "block";
    allSlides[0].className = "current";
    currentSlide = 0;
    currentChapter = -1;
    hideAll();
    processNavi();
}

function processNavi() {
    
    var h1_list = allSlides[currentSlide].querySelectorAll('h1');

    // 第一页、最后一页、包含h1的页面不显示导航
    if (h1_list[0] || currentSlide==0 || currentSlide == allSlides.length - 1) {
	navi.style.display = "none";
    } else {
	navi.style.display = "block";
	// 显示当前导航
	var naviItemList = navi.querySelectorAll('span');
	for(var i=0; i<naviItemList.length; i++) {
	    naviItemList[i].className = null;
	    naviItemList[currentChapter].className = "current";
	}
    }
}