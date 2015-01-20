$(document).ready(function() {


var opacity = .5
    $(".img-responsive").on({
        mouseenter: function () {
            $(this).parents(".inactive").removeClass("inactive");
            $(".inactive").stop().fadeTo(350, opacity);    
        },
        mouseleave: function () {
            $(".inactive").stop().fadeTo(350, 1);
            $(this).parents(".placeholder").addClass("inactive");
        }
    });
    
var margins = function(){
    if($('.big').length > 0){
        var rowHeight = $('.big').height();
        var imgDivHeight = $('.big').children('.placeholder').height();
        var textHeight = $('.big').children('.myhide').height();
        //console.log("text: " + textHeight + "img: " + imgDivHeight)
        if (textHeight > imgDivHeight) {
            rowHeight = textHeight + 20
            $('.big').css('height', rowHeight);
            $('.big').children('.myhide').css({'margin-top':'4px', 'margin-bottom':'10px'})
            var margin = ((textHeight-imgDivHeight)/2) + ((rowHeight-textHeight)/2)
            $('.big').children('.placeholder').css({'margin-top': margin, 'margin-bottom':margin})
        }
        else{
            rowHeight = imgDivHeight + 20
            $('.big').css('height', rowHeight);
            $('.big').children('.placeholder').css({'margin-top':'10px', 'margin-bottom':'10px'})
            var margin = ((imgDivHeight-textHeight)/2) + ((rowHeight-imgDivHeight)/2)
            $('.big').children('.myhide').css({'margin-top': margin, 'margin-bottom':margin})
        
        };
    };
};

$(window).resize(function() {
    
    margins();
    
    if ($('#-1').length) {
       $('#-1').attr('id', 0) 
    }
    if ($('.mobile').is(':visible')) {
        console.log("Now Mobile, Removing Big");
        if ($('.big').length > 0 && $('.big').attr('class').split(' ')[1] === "desk") {
            var numUP = $('.big').attr('class').split(' ')[2]
            console.log($('.big').attr('class').split(' ')[1])
            console.log("numUp: " + numUP);
            var toAddUP = ($('.mobile.'+numUP).find('.img-responsive'));
            toAddUP.parents('.placeholder').css('opacity', 1)
            console.log("toAddUp: " + toAddUP.html());
            removeBig(false);
            setTimeout(function(){
                big(toAddUP, true)
            }  ,100); 
            
        };
    }
    else {
        if ($('.big').length > 0 && $('.big').attr('class').split(' ')[1] === "mobile") {
            var numUP = $('.big').attr('class').split(' ')[2]
            console.log($('.big').attr('class').split(' ')[1])
            console.log("numUp: " + numUP);
            var toAddUP = ($('.desk.'+numUP).find('.img-responsive'));
            toAddUP.parents('.placeholder').css('opacity', 1)
            console.log("toAddUp: " + toAddUP.html());
            removeBig(false);
            setTimeout(function(){
                big(toAddUP, true)
            }  ,100); 
            
        };
    }
});  
 var tempScrollTop
$(document).on("click", function(e) {
    tempScrollTop = $(window).scrollTop();
    console.log(tempScrollTop);
/*Since Django doesn't have built in math tags, I used {% widthratio forloop.counter|add:'-3' 4 1 %}
as a divison hack. First it takes the forloop count and subtracts 3, then divids by 4 and rounds
to nearest interger. This sets the correct row for all but one case.when forloopcount = 1 - 3
= -.5 = -1. So replace -1 with 0 to put it in the right row.
1 - 3 = -2 / 4 = -.5 = -1
2 - 3 = -1/ 4 = -.25 = 0
3 - 3 = 0/ 4 = 0 = 0
4 - 3 = 1/ 4 = .25 = 0
5 - 3 = 2/ 4 = .5 = 1
6 - 3 = 3/ 4 = .75 = 1
7 - 3 = 4/ 4 = 1 = 1
8 - 3 = 5/ 4 = 1.25 = 1 */

    var targetRow= $(e.target).parents(".userProfile").attr('id');
    if ($('#-1').length) {
       $('#-1').attr('id', 0) 
    }
    if ($('#-1').length) {
       $('#-1').attr('id', 0) 
    }
        
    if ($('.big').length < 1){
        if ($(e.target).is('.img-responsive')) {    //There is no profile on display - create one
            big(e.target, true)                     //animation is set to true
        }
    }
    else {
        if ($(e.target).is('.selected')) { //if click on original profile that is being displayed
            removeBig(true)                //remove it.
        }
        else if ($(e.target).is('.img-responsive') && $(e.target).parent('.placeholder').parent('.big').length === 0) {  //if click on other profile replace it

            
            var bigRow = $('.big').attr('id');
            var addAni = false
            var removeAni = false
            //console.log ("Target Row: " + targetRow + " Big Row: " + bigRow);
            //console.log ("addAni: " + addAni + " removeAni: " + removeAni); 
            if (targetRow !== bigRow) { //checks to see if click element is in the
                addAni = true              //same row as the current big element
                removeAni = true            //if not, set animation for both add and remove to true
            };                          
            removeBig(removeAni)
            big(e.target, addAni)
        }
        else if ($(e.target).is('.close')){//($('.big').find(e.target).length)
         //allows user to click around big pic
           removeBig(true)
           //do nothing                                   // without removing it
        };
        //else //click anywhere else and big picture is removed.
       // {
        //    removeBig(true)
        //};
    };
});

    
/* This function controls the selection of specific user profiles
that have been clicked on. When a user clicks on a picture, we
pull out the row number the profile is in (from the div id) and clone
the profile div, adding it to the empty row above it. We animate it by 
fading the clone into the row while increasing its size. To increase 
it's size we need to add more room to the bootstrap column so we make it 
bigger and offset it to the center. We also add .selected class to the 
original div that the user clicked on.*/

    var big = function(target, animate){ //animate is a true/false var to set animation or not
        var ani = 0
        var fade = 400
        if (animate) {
            ani = 400
            fade = 750
        };
        var userProfileClone = $(target).parents('.placeholder').parents('.userProfile').clone();
        var userProfilePic = $(userProfileClone).children('.placeholder');
        var userProfileImg = $(userProfilePic).children(".img-responsive");
        var userProfileInfo = $(userProfileClone).children('.myhide');
        var rowNum = $(userProfileClone).attr('id');
        if ($('.mobile').is(':visible')) {
            var rowDiv = $("#mobilerow".concat(rowNum));
            console.log("media size")
        }
        else{
        var rowDiv = $("#row".concat(rowNum)); // get row number
        };
        //Will have to add this to html as hidden, so we can see if user has linkedin
        $(userProfilePic ).append( '<a href="#"><img src="https://cdn3.iconfinder.com/data/icons/sociocons/256/linkedin-sociocon.png" class="button1" style="height:33px;margin-right:10px" /></a>' );
        $(userProfilePic ).append( '<a href="#"><img src="http://icons.iconarchive.com/icons/graphicloads/100-flat-2/256/email-icon.png" class="button1" style="height:30px" /></a>' );


        $(rowDiv).children('.hideClose').css("display", "block")
        $(rowDiv).css('backgroundColor','#EEEEEE')
        $(rowDiv).css('marginBottom','5px')
        
        $(".img-responsive").off("mouseenter mouseleave");
        $('.placeholder').removeClass('cloned');
        $(target).parents('.placeholder').addClass('cloned');
        $('.inactive').not('.cloned').stop().fadeTo(350, opacity);

        $(".img-responsive").not('.cloned .img-responsive').on({  //have mouseevent all all 
            mouseenter: function () {
            $(this).parents(".inactive").stop().fadeTo(350, 1);
            $('.cloned').stop().fadeTo(300, opacity);
        },
        mouseleave: function () {
            $(this).parents(".inactive").not('.cloned').stop().fadeTo(350, opacity);
            $('.cloned').stop().fadeTo(300, 1);
        }
        });
        
        $(userProfileImg).height(300);
        $(userProfileInfo).css({'display':'block',"fontSize":"1.1em"});
        if (userProfileInfo.length===0) {
            $(userProfilePic).removeClass("col-sm-3").addClass("col-md-4 col-md-offset-4 col-xs-offset-3")
        }
        else{
            $(userProfilePic).removeClass("col-sm-3").addClass("col-md-4 col-md-offset-1")
        };
        $(userProfileClone).hide().appendTo(rowDiv).fadeIn(fade);

        $(userProfileClone).addClass("big")  // div and center it
        $(target).addClass("selected")
        $(userProfileClone).parents('.hidden-row').height(0);
        margins()
        $(userProfileClone).parents('.hidden-row').animate({
            height: "425px",
        }, ani,function() {
            $(userProfileClone).parents('.hidden-row').css({"height":"100%"});
        })
        $(userProfileImg).animate({ //increase profile image size
        height: "300px",
        borderWidth: "10px",
        }, ani );
        //$('.myhide').animate({ //increase profile image size and wait until div are properly sized then center with margins
        //    fontSize: "1.1em",
        //    }, ani, function() {
        //        margins()
        // });
        console.log("In function Position: " + tempScrollTop + " big height: "+ $('.big').height())
        $(window).scrollTop(tempScrollTop);
    }

/* This function controls removal/change of specific user
profiles that have been clicked on. When there is a profile being displayed and 
a user click on a picture, we remove the .big div and get rid of .selected
we animate when the user hasn't click on a profile in the same row as the current one.*/

    var removeBig = function(animate){
        
        $('.hideClose').css("display", "none")
        $('.big').addClass('remove').removeClass('big');
        $(".img-responsive").parents('.placeholder').stop().fadeTo(350, 1);
        $(".img-responsive").parents('.placeholder').addClass("inactive");
        $(".cloned").removeClass("cloned");
        $(".img-responsive").on({
            mouseenter: function () {
                $(this).parents(".inactive").removeClass("inactive");
                $(".inactive").not('.remove').stop().fadeTo(350, opacity);    
            },
            mouseleave: function () {
                $(".inactive").stop().fadeTo(350, 1);
                $(this).parents(".placeholder").addClass("inactive");
            }
        });
        
        if (animate) {
            $('.remove').fadeTo(100, opacity, function(){
                $('.remove').animate({
                    height: "0px",
                    //fontSize: ".1em",
                    //borderWidth: "10px",
                }, 400, function(){
                    //$('.placeholder').removeClass('cloned');
                        $('.selected').removeClass('selected');
                        $('.remove').remove();
                })
            });
        }
        else {
            $('.selected').removeClass('selected');
            $('.remove').remove();
        };
    }
    

    
});

