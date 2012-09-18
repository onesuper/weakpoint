/*
 * weakpoint.js
 * (c) 2012 onesuper
 */


function weakPoint() {
    var allSlides = $('.paper');
    var navi = $('.navi')[0];
    var currentSlide = 0;
    var currentChapter = -1;

    this.init = function() {
	    addEventListeners();
	    currentSlide = 0;
	    currentChapter = -1;
	    processNavi();
	    popupIn();
	    popupOut();
    }

    function addEventListeners() {
	    document.addEventListener('keydown', onKeyDown, false);
    }

    function onKeyDown(event) {
	    switch(event.keyCode) {
	    case 33: case 37: case 80: case 75: previous(); break;
	    case 34: case 39: case 78: case 74: next(); break;    
	    case 36: reset(); break;
	    }
    }

    function next() {
        
	    // end
	    if (currentSlide == allSlides.length - 1)
	        return;

        if (onSwitch == true)
            return;

        
	    //set current chapter
	    var h1_list = allSlides[currentSlide+1].querySelectorAll('h1');
	    if (h1_list[0]) {
	        currentChapter += 1;
	    }
	    
	    currentSlide += 1;
	    bxslide.goToNextSlide();
	    processNavi();
        
    }

    function previous() {
	    
	    if (currentSlide == 0)
	        return;
        if (onSwitch == true)
            return;


	    //进入新的章节
	    var h1_list = allSlides[currentSlide].querySelectorAll('h1');
	    if (h1_list[0]){	
	        currentChapter -= 1;
	    }
	    currentSlide -= 1;
       
	    bxslide.goToPreviousSlide();
	    processNavi();
       
    }

    function reset() {
        if (onSwitch == true)
            return;
	    currentSlide = 0;
	    currentChapter = -1;
	    bxslide.goToFirstSlide();
	    processNavi();
    }

    function processNavi() {
	    // 第一页、最后一页不显示导航
	    if (currentSlide==0 || currentSlide == allSlides.length - 1) {
	        navi.style.display = "none";
	    } else {
	        navi.style.display = "block";
	        // 当前章节
	        var naviItemList = navi.querySelectorAll('span');
	        for(var i=0; i<naviItemList.length; i++) {
		        naviItemList[i].className = null;
		        naviItemList[currentChapter].className = "current";
	        }
	    }
    }

    function popupIn() {
	    $("#popup").fadeIn(1000);

	    
    }

    function popupOut() {
	    $("#popup").fadeOut(6000);
    }

}