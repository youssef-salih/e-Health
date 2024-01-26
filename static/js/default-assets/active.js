(function($) {
  'use strict';
  var dento_window = $(window);

  dento_window.on('load', function() {
    $('#preloader').fadeOut('1000', function() {
      $(this).remove();
    });
  });


  if($.fn.classyNav) {
    $('#cardioNav').classyNav();
  }

  if($.fn.owlCarousel) {
    var welcomeSlider = $('.welcome-slides');
    welcomeSlider.owlCarousel({
      items: 1,
      loop: true,
      autoplay: true,
      smartSpeed: 1500,
      nav: true,
      navText: ["<i class='ti-angle-left'</i>", "<i class='ti-angle-right'</i>"],
      dots: true,
      animateIn: 'fadeIn',
      animateOut: 'fadeOut'
    })
    welcomeSlider.on('translate.owl.carousel', function() {
      var layer = $("[data-animation]");
      layer.each(function() {
        var anim_name = $(this).data('animation');
        $(this).removeClass('animated ' + anim_name).css('opacity', '0');
      });
    });
    $("[data-delay]").each(function() {
      var anim_del = $(this).data('delay');
      $(this).css('animation-delay', anim_del);
    });
    $("[data-duration]").each(function() {
      var anim_dur = $(this).data('duration');
      $(this).css('animation-duration', anim_dur);
    });
    welcomeSlider.on('translated.owl.carousel', function() {
      var layer = welcomeSlider.find('.owl-item.active').find("[data-animation]");
      layer.each(function() {
        var anim_name = $(this).data('animation');
        $(this).addClass('animated ' + anim_name).css('opacity', '1');
      });
    });
  }



  if(dento_window.width() > 767) {
    new WOW().init();
  }



  if($.fn.jarallax) {
    $('.jarallax').jarallax({
      speed: 0.2
    });
  }


  if($.fn.scrollUp) {
    dento_window.scrollUp({
      scrollSpeed: 800,
      scrollText: '<i class="arrow_up"</i>'
    });
  }

})(jQuery);
