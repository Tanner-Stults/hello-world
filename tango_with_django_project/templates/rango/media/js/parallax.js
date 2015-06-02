$(document).ready(function(e) {
  parallax();
  reorient(e);

  window.addEventListener("orientationchange", function(){
    reorient(e)
    }, false);
  
function reorient(e){ //prevents scrolling in landscape
    var portrait = (window.orientation % 180 == 0);
    if (window.orientation != null) {
      if (portrait == false) {
        $('.rotate').css({'display':'none'});
        $('.rotateError').css({'display':'block'});
        document.ontouchstart = function(e){ 
        e.preventDefault();
        }
      }else{
        $('.rotate').css({'display':'block'});
        $('.rotateError').css({'display':'none'});
        document.ontouchstart = function(e){ 
        }
      }
    }
  }
});
  function debounce(func, wait, immediate) {
  //console.log("in debounce");
  var timeout;
    return function() {
      var context = this;
      var args = arguments;
      var later = function(){
        timeout = null;
        if (!immediate){
          func.apply(context, args);
        }
      };
      var callNow = immediate && !timeout;
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
      if (callNow){
        func.apply(context, args);
      }
    }
  }

// Returns a function, that, as long as it continues to be invoked, will not
// be triggered. The function will be called after it stops being called for
// N milliseconds. If `immediate` is passed, trigger the function on the
// leading edge, instead of the trailing.


function parallax() {
  console.log("in parallax");
    /*  Globals
    -------------------------------------------------- */
    var PROPERTIES =              ['translateX', 'translateY', 'opacity', 'rotate', 'scale'],
      $window =                   $(window),
      $body =                     $('body'),
      wrappers =                  [],
      currentWrapper =            null,
      scrollTimeoutID =           0,
      bodyHeight =                0,
      windowHeight =              0,
      windowWidth =               0,
      prevKeyframesDurations =    0,
      scrollTop =                 0,
      relativeScrollTop =         0,
      currentKeyframe =           0,
      keyframes = [
        {
          'wrapper' : '#intro',
          'duration' : '50%',
          'animations' :  [
            {
              'selector'    : '.main-logo',
              'translateX'  : 0,
              'scale'       : 1,
              'opacity'     : 1
            },
            {
              'selector'    : '#tagline',
              'translateY'  : 0,
              'translateX'  : 0,
              'scale'       : 1
            }
          ]
        },{
          'wrapper' : '#intro',
          'duration' : '100%',
          'animations' :  [
            {
              'selector'    : '#tagline',
              'scale'       : 0.6,
              'opacity'     : 0
            },{
              'selector'    : '.main-logo',
              'scale'       : 0.9,
              'opacity'     : 0
            }
        ]
        },{
          'wrapper' : '#featured',
          'duration' : '120%',
          'animations' :  [
            {
              'selector'    : '.featured',
              'translateY'  : ['100%','35%'],
              'scale'     : [1, 1.3],
              'opacity'     : [0, 1.75] // hack to accelrate opacity speed
            } 
          ]
        },{
          'wrapper' : '#featured',
          'duration' : '80%',
          'animations' :  [
             {
              'selector'    : '.featured',
              'translateY'  : ['35%','-30%'],
              'scale'       : [1.3, 1]
            }
          ]
          } , {
          'wrapper' : '#slides',
          'duration' : '100%',
          'animations' :  [
            {
              'selector'    : '.slideText1',
              'translateY'  : ['100%','7%'],
              'opacity'     : [0.6, 1] // hack to accelrate opacity speed
            },
            {
              'selector'    : '.slide1',
              'translateY'  : ['107%','28%'],
              'opacity'     : [0.6, 1] // hack to accelrate opacity speed
            },
            {
              'selector'    : '.hide1',
              'opacity'     : [0, 0] // hack to accelrate opacity speed
            },
            {
            'selector'    : '.hide2',
              'opacity'     : [0, 0] // hack to accelrate opacity speed
            }
          ]
          } , {
          'wrapper' : '#slides',
          'duration' : '100%',
          'animations' :  [
            {
              'selector'    : '.slideText2',
              'translateY'  : ['100%','13%'],
              'opacity'     : [0.6, 1] // hack to accelrate opacity speed
            },
            {
              'selector'    : '.slide2',
              'translateY'  : ['113%','32%'],
              'opacity'     : [0.6, 1] // hack to accelrate opacity speed
            },
            {
            'selector'    : '.hide2',
              'opacity'     : [0, 0] // hack to accelrate opacity speed
            }
          ]
          }, {
          'wrapper' : '#slides',
          'duration' : '100%',
          'animations' :  [
            {
              'selector'    : '.slideText3',
              'translateY'  : ['100%','19%'],
              'opacity'     : [0.6, 1] // hack to accelrate opacity speed
            },
            {
              'selector'    : '.slide3',
              'translateY'  : ['119%','36%'],
              'opacity'     : [0.6, 1] // hack to accelrate opacity speed
            }
          ]
          }, {
            'wrapper' : '#slides',
            'duration' : '20%',
            'animations' :  []
          },{
          'wrapper' : '#slides',
          'duration' : '100%',
          'animations' :  [
            {
              'selector'    : '.slide1',
              'translateY'  : ['28%','-100%'],
              'translateX'  : '10%',
              'rotate'      : 15,
              'opacity'     : [1, 0.3] // hack to accelrate opacity speed
            },{
              'selector'    : '.slideText1',
              'translateY'  : ['7%','-100%'],
              'translateX'  : '10%',
              'rotate'      : 15,
              'opacity'     : [1, 0.3] // hack to accelrate opacity speed
            }, {
              'selector'    : '.slide2',
              'translateY'  : ['32%','-100%'],
              'rotate'      : 30,
              'opacity'     : [1, 0.3] // hack to accelrate opacity speed
            }, {
              'selector'    : '.slideText2',
              'translateY'  : ['13%','-100%'],
              'rotate'      : 30,
              'opacity'     : [1, 0.3] // hack to accelrate opacity speed
            }, {
              'selector'    : '.slide3',
              'translateY'  : ['36%','-100%'],
              'translateX'  : '-10%',
              'rotate'      : 45,
              'opacity'     : [1, 0.3] // hack to accelrate opacity speed
            }, {
              'selector'    : '.slideText3',
              'translateY'  : ['19%','-100%'],
              'translateX'  : '-10%',
              'rotate'      : 45,
              'opacity'     : [1, 0.3] // hack to accelrate opacity speed
            }
          ]
          },{
            'wrapper' : '#database',
            'duration' : '150%',
            'animations' :  [
              {
                'selector'    : '#domExplosionListHeader',
                'translateY'  : ['100%','5%'],
                'opacity'     : [0, 1] // hack to accelrate opacity speed
              } , {
                'selector'    : '#domExplosionList',
                'translateY'  : ['100%','24%'],
                'opacity'     : [0, 1] // hack to accelrate opacity speed
              },{
                'selector'    : '.dei-1',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-2',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-3',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-4',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-5',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-6',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-7',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-8',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-9',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-10',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-11',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-12',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-13',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-14',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-15',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-16',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-17',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-18',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-19',
                'opacity'     : 1,
              },{
                'selector'    : '.dei-20',
                'opacity'     : 1,
              }
            ]
          } , {
            'wrapper' : '#database',
            'duration' : '150%',
            'animations' :  [
              {
                'selector'    : '#domExplosionListHeader',
                'translateY'  : ['5%','-30%'],
                'scale'     : [1, 1.3], // hack to accelrate opacity speed
              } ,{
                'selector'    : '#domExplosionList',
                'opacity'   : 1,
                'translateY'  : ['24%','24%'],
              },{
                'selector'    : '.dei-1',
                'translateY'  : '-15%',
                'translateX'  : '-10%',
                'opacity'     : [1, 0],
                'scale'       : 2,
              } , {
                'selector'    : '.dei-2',
                'translateY'  : '-5%',
                'translateX'  : '-4%',
                'opacity'     : [1, 0] // hack to decelrate opacity speed
              } , {
                'selector'    : '.dei-3',
                'translateY'  : '-9%',
                'translateX'  : '2%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.2,
              } , {
                'selector'    : '.dei-4',
                'translateY'  : '-17%',
                'translateX'  : '8%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.5,
              } , {
                'selector'    : '.dei-5',
                'translateY'  : '-2%',
                'translateX'  : '-15%',
                'opacity'     : [1, 0],
                'scale'       : 2,
              } , {
                'selector'    : '.dei-6',
                'translateY'  : '-1%',
                'translateX'  : '-7%',
                'opacity'     : [1, 0], // hack to decelrate opacity speed
                'scale'       : 1.2,
              } , {
                'selector'    : '.dei-7',
                'translateY'  : '-4%',
                'translateX'  : '2%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.1,
              } , {
                'selector'    : '.dei-8',
                'translateY'  : '-3%',
                'translateX'  : '12%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.8,
              }, {
                'selector'    : '.dei-9',
                'translateY'  : '3%',
                'translateX'  : '-12%',
                'opacity'     : [1, 0],
                'scale'       : 1.5,
              } , {
                'selector'    : '.dei-10',
                'translateY'  : '5%',
                'translateX'  : '-4%',
                'opacity'     : [1, 0] // hack to decelrate opacity speed
              } , {
                'selector'    : '.dei-11',
                'translateY'  : '8%',
                'translateX'  : '6%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.4,
              } , {
                'selector'    : '.dei-12',
                'translateY'  : '1%',
                'translateX'  : '20%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.9,
              } , {
                'selector'    : '.dei-13',
                'translateY'  : '8%',
                'translateX'  : '-12%',
                'opacity'     : [1, 0],
                'scale'       : 1.8,
              } , {
                'selector'    : '.dei-14',
                'translateY'  : '4%',
                'translateX'  : '-3%',
                'opacity'     : [1, 0], // hack to decelrate opacity speed
                'scale'       : 1.3,
              } , {
                'selector'    : '.dei-15',
                'translateY'  : '14%',
                'translateX'  : '5%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.7,
              } , {
                'selector'    : '.dei-16',
                'translateY'  : '6%',
                'translateX'  : '9%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 2,
              }, {
                'selector'    : '.dei-17',
                'translateY'  : '8%',
                'translateX'  : '-12%',
                'opacity'     : [1, 0],
                'scale'       : 1.8,
              } , {
                'selector'    : '.dei-18',
                'translateY'  : '4%',
                'translateX'  : '3%',
                'opacity'     : [1, 0], // hack to decelrate opacity speed
                'scale'       : 1.3,
              } , {
                'selector'    : '.dei-19',
                'translateY'  : '14%',
                'translateX'  : '5%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 1.7,
              } , {
                'selector'    : '.dei-20',
                'translateY'  : '6%',
                'translateX'  : '9%',
                'opacity'     : [1, 0], // hack to accelrate opacity speed
                'scale'       : 2,
              }
            ]
          },{
            'wrapper' : '#quotes',
            'duration' : '100%',
            'animations' :  [
              {
                'selector'    : '#quote1',
                'opacity'     : [0.5, 1],
                'translateY'  : ['100%','10%'],
              } , {
                'selector'    : '#quote2',
                'opacity'     : [0.5, 1],
                'translateY'  : ['100%','37%'],
              } , {
                'selector'    : '#quote3',
                'opacity'     : [0.5, 1],
                'translateY'  : ['100%','64%'],
              } 
            ]
          },  {
            'wrapper' : '#quotes',
            'duration' : '80%',
            'animations' :  [
              {
                'selector'    : '#quote1',
                'scale'     : [1, 1.2],
                'translateY'  : ['10%','-55%'],
              }
              ]
          },  {
            'wrapper' : '#quotes',
            'duration' : '85%',
            'animations' :  [
              {
                'selector'    : '#quote2',
                'scale'     : [1, 1.2],
                'translateY'  : ['37%','-55%'],
              }
              ]
          },  {
            'wrapper' : '#quotes',
            'duration' : '95%',
            'animations' :  [
              {
                'selector'    : '#quote3',
                'scale'     : [1, 1.2],
                'translateY'  : ['64%','-55%'],
              } 
              ]
          },{
            'wrapper' : '#contact',
            'duration' : '120%',
            'animations' :  [
               {
                'selector'    : '.contact',
                'opacity'     : [0,1],
                'scale'       : [0, 1]
              }
            ]
          }, {
            'wrapper' : '#contact',
            'duration' : '100%',
            'animations' :  []
          }
  ]
        
    /*  Construction
    -------------------------------------------------- */

    /**
     * Used scrollIntervalID = setInterval(updatePage, 10);, but causes
     * animateElement to be called every .01 seconds and was too resource
     * intensive. Instead have onScroll event that calls animateElement and
     * forceDrawUpdate for refreshes
     */
    init = function() {
      height1 =  window.innerHeight;
      setupValues();
      $window.resize(throwError)
      if(isTouchDevice) {
        $window.resize(throwError)
      }
      forceDrawUpdate();
      /*document.addEventListener("touchmove", scrollMove);
      document.addEventListener("touchend", scrollEnd);
      document.addEventListener("touchstart", scrollStart);*/
      hideNonCurrentWrappers();
      hideOffScreen();
    }

    hideOffScreen = function(){ //hide elements that are off screen on refresh
      for(i=0;i<keyframes.length;i++) {
        for(j=0;j<keyframes[i].animations.length;j++) {
          animation   = keyframes[i].animations[j];
          if($(animation.selector).isOnScreen(0.01,0.01) == false){
            //console.log(animation.selector + ": offScreen");
            $(animation.selector).css({
              'opacity': 0,
            })
          }
        }
      }
    }
    setupValues = function() {
      scrollTop = $window.scrollTop();//window.pageYOffset; //$('body').scrollTop();
      windowHeight = $(window).height();
      windowWidth = $(window).width();
      convertAllPropsToPx();
      buildPage();
    }

    buildPage = function() {//Adds the duration (which has been converted to px) 
      var i, j, k;          //of each transition to the body height
      for(i=0;i<keyframes.length;i++) { // loop keyframes 
        bodyHeight += keyframes[i].duration;
        if($.inArray(keyframes[i].wrapper, wrappers) == -1) {
          wrappers.push(keyframes[i].wrapper); //populate the global array wrappers with each keyframe
        }
        for(j=0;j<keyframes[i].animations.length;j++) { // loop animations
          Object.keys(keyframes[i].animations[j]).forEach(function(key) { // loop properties
            value = keyframes[i].animations[j][key];
            if(key !== 'selector' && value instanceof Array === false) { //convert single numbers to array
              var valueSet = [];                                         //with starting value = to default
              valueSet.push(getDefaultPropertyValue(key), value);
              value = valueSet;
            }
            keyframes[i].animations[j][key] = value; //update value
          });
        }
      }
      $body.height(bodyHeight);
      $window.scroll(0);//TODO: See if this is what is causing iphone refresh to start at top
      currentWrapper = wrappers[0];;
      $(currentWrapper).show();
    }

    convertAllPropsToPx = function() { //Looks only for translateY and translateX and changes % to px
      var i, j, k;                     //With duration and px, know how fast to translate element
      for(i=0;i<keyframes.length;i++) { // loop keyframes
        keyframes[i].duration = convertPercentToPx(keyframes[i].duration, 'y');
        for(j=0;j<keyframes[i].animations.length;j++) { // loop animations
          Object.keys(keyframes[i].animations[j]).forEach(function(key) { // loop properties
            value = keyframes[i].animations[j][key];
            if(key !== 'selector') {
              if(value instanceof Array) { // if its an array
                for(k=0;k<value.length;k++) { // if value in array is %
                  if(typeof value[k] === "string") {
                    if(key === 'translateY') {
                      value[k] = convertPercentToPx(value[k], 'y');
                    } else {
                      value[k] = convertPercentToPx(value[k], 'x');
                    }
                  }
                } 
              } else {
                if(typeof value === "string") { // if single value is a %
                  if(key === 'translateY') {
                    value = convertPercentToPx(value, 'y');
                  } else {
                    value = convertPercentToPx(value, 'x');
                  }
                }
              }
              keyframes[i].animations[j][key] = value;
            }
          });
        }
      }
    }
    
    getDefaultPropertyValue = function(property) {
      switch (property) {
        case 'translateX':
          return 0;
        case 'translateY':
          return 0;
        case 'scale':
          return 1;
        case 'rotate':
          return 0;
        case 'opacity':
          return 1;
        default:
          return null;
      }
    }

    /*  Animation/Scrolling
    -------------------------------------------------- */

    $(window).scroll(function(){
      window.requestAnimationFrame(function() {
        scrolTopPrev = scrollTop; //FF & safari don't set scrollTop until scroll so check here
        setScrollTops();
        if (scrolTopPrev == 0 && scrollTop != 0) {
          forceDrawUpdate();
        }
  
        if(scrollTop > 0 && scrollTop <= (bodyHeight - windowHeight)) {
          animateElements();
          setKeyframe();
          //hideNonCurrentWrappers();
        }
      });
    })

    forceDrawUpdate = function() { //animateElements only works with scroll... 
      for(var i=0; i<20; i++){    //force 50 animations (On refresh etc.)
        setScrollTops();
        if(scrollTop >= 0 && scrollTop <= (bodyHeight - windowHeight)) {
          animateElements();
          setKeyframe();
        }
      }
    }

    setScrollTops = function() {
      //console.log("page offset: " + window.pageYOffset + " with offset: " + (window.pageYOffset + 15))
      scrollTop = $window.scrollTop(); //Better than $('body').scrollTop() for mobile
      relativeScrollTop = scrollTop - prevKeyframesDurations;
      }

    animateElements = function() { //TODO: Find out why .tagline has random scale
      //console.log("--relativeScrollTop: " + relativeScrollTop + "--ScrollTop: " + scrollTop +" --- prevKey: " + prevKeyframesDurations+" --- currentKeyFrame: " + currentKeyframe +" --- duration: " + keyframes[currentKeyframe].duration);
      var animation, translateY, translateX, scale, rotate, opacity;
      for(var i=0;i<keyframes[currentKeyframe].animations.length;i++) {
        animation   = keyframes[currentKeyframe].animations[i];
        translateY  = calcPropValue(animation, 'translateY');
        translateX  = calcPropValue(animation, 'translateX');
        scale       = calcPropValue(animation, 'scale');
        rotate      = calcPropValue(animation, 'rotate');
        opacity     = calcPropValue(animation, 'opacity');
        $(animation.selector).css({
          'transform':    'translate3d(' + translateX +'px, ' + translateY + 'px, 0) scale('+ scale +') rotate('+ rotate +'deg)',
          'opacity' : opacity,
        })
      }
    }

    calcPropValue = function(animation, property) {
      var value = animation[property];
      if(value) {
        value = easeInOutQuad(relativeScrollTop, value[0], (value[1]-value[0]), keyframes[currentKeyframe].duration);
      } else {
        value = getDefaultPropertyValue(property);
      }
      // value = +value.toFixed(2) 
      // TEMPORARILY REMOVED CAUSE SCALE DOESN'T WORK WITH AN AGRESSIVE ROUNDING LIKE THIS
      return value;
    }
    
    /** 
    @t is the current time (or position) of the tween. In px
    @b is the beginning value of the property.
    @c is the change between the beginning and destination value of the property.
    @d is the total time of the tween.
    For lin In : return c*t/d + b;
    **/
    easeInOutQuad = function (t, b, c, d) { //Sin easing accelerating via Sin until half then deccelerate
      //Sin in/out
      return -c/2 * (Math.cos(Math.PI*t/d) - 1) + b;
      

    };

    setKeyframe = function() { //checks to see if scrolled past the relative duration of the animation
      if(scrollTop > (keyframes[currentKeyframe].duration + prevKeyframesDurations)) {
        prevKeyframesDurations += keyframes[currentKeyframe].duration;
        prevKeyframesDurations1 = prevKeyframesDurations;
        currentKeyframe++;
        showCurrentWrappers();
      } else if(scrollTop <= prevKeyframesDurations) {
        if (currentKeyframe > 0) {
        currentKeyframe--;
        //console.log(currentKeyframe);
        prevKeyframesDurations -= keyframes[currentKeyframe].duration;
        showCurrentWrappers();
        }
      }
    }

    showCurrentWrappers = function() {
      if(keyframes[currentKeyframe].wrapper != currentWrapper) {
        $(currentWrapper).hide();
        //console.log("hiding")
        /*for(j=0;j<keyframes[currentKeyframe-1].animations.length;j++) {
          animation   = keyframes[currentKeyframe-1].animations[j];
            //console.log("Hiding: " + animation.selector);
            $(animation.selector).css({
              'opacity': 0,
              'transform': '',
            })
        }
        for(j=0;j<keyframes[currentKeyframe+1].animations.length;j++) {
          animation   = keyframes[currentKeyframe+1].animations[j];
            //console.log("Hiding: " + animation.selector);
            $(animation.selector).css({
              'opacity': 0,
              'transform': '',
            })
        }*/
        $(keyframes[currentKeyframe].wrapper).show();
        currentWrapper = keyframes[currentKeyframe].wrapper;
      }
    }
    
    hideNonCurrentWrappers = function() {
      for(var i = 0; i < keyframes.length; i++){
        if(keyframes[i].wrapper != currentWrapper) {
          $(keyframes[i].wrapper).hide();
        }else{
          $(keyframes[i].wrapper).show();
        }
      }
    }

    /*  Helpers
    -------------------------------------------------- */

    convertPercentToPx = function(value, axis) {
      if(typeof value === "string" && value.match(/%/g)) { //only need to convert %, else already px
        if (windowHeight < 650) { //assumption: window hieght will not be less than 650px
          computedWindowHeight = 650;
        }else{
          computedWindowHeight = windowHeight
        }
        if(axis === 'y') value = (parseFloat(value) / 100) * computedWindowHeight;
        if(axis === 'x') value = (parseFloat(value) / 100) * windowWidth;
      }
      return value;
    }

    throwError = function() {
      $body.addClass('page-error')
    }

    isTouchDevice = function() {
      return 'ontouchstart' in window // works on most browsers 
      || 'onmsgesturechange' in window; // works on ie10
    }
    //console.log("at bottom");
    init();
}


