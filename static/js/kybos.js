	/* JS kybos */

$(document).ready(function() {
    procslider();
});

/*NAV*/

$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure to proceed?');
});


		/*NAV BEING FIXED*/


$(document).on('scroll',function(){
	if($(document).scrollTop()>200){
		$("header").addClass('fixed');
		$("#headertop").addClass('hidden');


	}else{
		$("header").removeClass('fixed');
		$("#headertop").addClass('show');
	};

});

		/*NAV LINKS*/

$(".navbar-default .navbar-nav li a").click(function(){
	var scrollAnchor = $(this).attr("data-scroll");
	var	scrollPoint = $("section[data-anchor='"+scrollAnchor+"']").offset().top - 70;

	$("body,html").animate({scrollTop: scrollPoint},500);
	return false;
});





/*Slider concept*/

$('#concept_slider').carousel({interval:4000});


/*Process or me*/

$("#1").on("click",function(){
	$("#proceso").fadeOut(250,function(){
		$("#proceso").removeClass("on");
		$("#2").removeClass("subon");
	});
	$("#me").delay(250).fadeIn(250,function(){
		$("#me").addClass("on");
		$("#1").addClass("subon");
	});
});

$("#2").on("click",function(){
	$("#me").fadeOut(250,function(){
		$("#me").removeClass("on");
		$("#1").removeClass("subon");

	});
	$("#proceso").delay(250).fadeIn(250,function(){
		$("#proceso").addClass("on");
		$("#2").addClass("subon");
	});
});



/*Slider process*/ 

function procslider(){
	$('.texts').first().addClass('textactive');
	$('#imgslider img').first().addClass('imgactive');

	$('.glyphicon-chevron-right, .glyphicon-chevron-left').click(function(){
		var $this = $(this),
			curtextactive = $('#textwrap').find('.textactive'),
			textposition = $('#textwrap').children().index(curtextactive),
			numtext = $('.texts').length;

		var	curimgactive = $('#imgslider').find('.imgactive'),
			imgposition = $('#imgslider').children().index(curimgactive),
			numimg = $('.img').length;

		if ($this.hasClass('glyphicon-chevron-right')){
			if (textposition < numtext - 1){
				$('.textactive').removeClass('textactive').next().addClass('textactive');
				} else {
				$('.texts').removeClass('textactive').first().addClass('textactive');
				}; 
			} else {
				if (textposition == 0){
					$('.textactive').removeClass('textactive').last().addClass('textactive');
				} else {
				$('.textactive').removeClass('textactive').prev().addClass('textactive');
				};
			};

		if ($this.hasClass('glyphicon-chevron-right')){
			if (imgposition < numimg - 1){
				$('.imgactive').removeClass('imgactive').next().addClass('imgactive');
				} else {
				$('.img').removeClass('imgactive').first().addClass('imgactive');
				}; 
			} else {
				if (imgposition == 0){
				$('.imgactive').removeClass('imgactive').last().addClass('imgactive');
			} else {
				$('.imgactive').removeClass('imgactive').prev().addClass('imgactive');
				};
			}	
	});


}



		/*FOOTER LINKS*/

$(".footerboxcenter ul li a").click(function(){
	var scrollAnchor = $(this).attr("data-scroll");
	var	scrollPoint = $("section[data-anchor='"+scrollAnchor+"']").offset().top - 70;

	$("body,html").animate({scrollTop: scrollPoint},500);
	return false;
});





/*ANIMATIONS*/


jQuery(function($) {
  
  var doAnimations = function() {
    
    // Calc current offset and get all animatables
    var offset = $(window).scrollTop() + $(window).height(),
        $animatables = $('.animatable');
    
 
    
    // Check all animatables and animate them if necessary
		$animatables.each(function(i) {
       var $animatable = $(this);
			if (($animatable.offset().top + $animatable.height()-200) < offset) {
        $animatable.removeClass('animatable').addClass('animated');
			}
    });

	};
  
  // Hook doAnimations on scroll, and trigger a scroll
	$(window).on('scroll', doAnimations);
  $(window).trigger('scroll');

});


//PRODUCTS DETAILS


$(document).ready(function() {
    slider();
});
/* Putting small image into the big img place */

function slider(){
	$('.big').first().addClass('bigimg_active');
	$('.small').first().addClass('smallimg_active');

	$('.small').click(function(){
		var	$this = $(this),
			$siblings = $(this).parent().children(),
			position = $siblings.index($this);
		$('.big').removeClass('bigimg_active').eq(position).addClass('bigimg_active');
		$siblings.removeClass('smallimg_active');
		$(this).addClass('smallimg_active');
	});

	$('.glyphicon-chevron-right, .glyphicon-chevron-left').click(function(){
		var $this = $(this),
			curbigactive = $('#bigimg').find('.bigimg_active'),
			bigposition = $('#bigimg').children().index(curbigactive),
			bignum = $('.big').length;

		if($this.hasClass('glyphicon-chevron-right')){
			if (bigposition < bignum - 1){
				$('.bigimg_active').removeClass('bigimg_active').next().addClass('bigimg_active');
				$('.smallimg_active').removeClass('smallimg_active').next().addClass('smallimg_active');
			} else {
				$('.big').removeClass('bigimg_active').first().addClass('bigimg_active');
				$('.small').removeClass('smallimg_active').first().addClass('smallimg_active');
			};
		} else {
			if (bigposition == 0){
				$('.big').removeClass('bigimg_active').last().addClass('bigimg_active');
				$('.small').removeClass('smallimg_active').last().addClass('smallimg_active');
			} else {
				$('.bigimg_active').removeClass('bigimg_active').prev().addClass('bigimg_active');
				$('.smallimg_active').removeClass('smallimg_active').prev().addClass('smallimg_active');
			};
		};
	});
};

