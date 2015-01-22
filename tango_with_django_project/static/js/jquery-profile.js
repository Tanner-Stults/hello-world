$(document).ready(function() {
  
    $('#work_experience_add').click(function(event) {
        $('.work_experience_form, .work_experience_submit').show();
        $('#work_experience_add').hide()
  
    });
    $('#education_add').click(function(event) {
        $('.education_form, .education_submit').show();
        $('#education_add').hide()
  
    });
        
    $('#work_experience_cancel').click(function(event) {
        $('.work_experience_form, .work_experience_submit').hide();
        $('#work_experience_add').show()
    });
    
    $('#education_cancel').click(function(event) {
        $('.education_form, .education_submit').hide();
        $('#education_add').show()
    });
    
    $('.work_experience_edit').click(function(event) {
        expNum = $(this).attr('id');
        $(this).parents('.feed-card').hide();
        $('[data-edit='+expNum+'].edit_work_experience_form').removeClass("hide");
    });
    
    $('.education_edit').click(function(event) {
        expNum = $(this).attr('id');
        $(this).parents('.feed-card').hide();
        $('[data-edit='+expNum+'].edit_education_form').removeClass("hide");
    });
    
    $("#work_experience_success").click( function(event) {
        $("#workExperience_form").submit(); 
    });
    
    $("#education_success").click( function(event) {
        $("#education_form").submit(); 
    });
    
    $("#initial_work_experience_success").click( function(event) {
        $("#initial_workExperience_form").submit(); 
    });
    $(".education_delete").click( function(event) {
        formNum = $(this).attr("id");
        window.location.href = "/cornell/delete_education/"+formNum;
    });
    $(".work_experience_delete").click( function(event) {
        formNum = $(this).attr("id");
        window.location.href = "/cornell/delete_workExperience/"+formNum;
    });
    $(".work_experience_save").click( function(event) {
        formNum = $(this).attr("id");
        $("#editWorkExperience_form"+formNum).submit(); 
    });

    
    $(".work_experience_cancel").click( function(event) {
        expNum = $(this).attr('id');
        $(this).parents('.feed-card').prev('.display').show();
        $('[data-edit='+expNum+'].edit_work_experience_form').addClass("hide");
    });
    
    $(".education_cancel").click( function(event) {
        expNum = $(this).attr('id');
        $(this).parents('.feed-card').prev('.display').show();
        $('[data-edit='+expNum+'].edit_education_form').addClass("hide");
    });
    $('.change_pic, .thumb').mouseenter(function(){
        $('.change_pic').stop().animate({
         backgroundColor: 'rgba(0,0,0,0.8)'},300);
        $('<p class="change_pic_text">Change&nbsp</p>').insertBefore('.change_pic_img')
        $('<p class="change_pic_text">&nbspPicture&nbsp</p>').insertAfter('.change_pic_img')
    });
    $('.change_pic, .thumb').mouseleave(function(){
        $('.change_pic').stop().animate({
         backgroundColor: 'rgba(0,0,0,0.5)'},300);
        $('.change_pic_text').remove();
        
    });
});