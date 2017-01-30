//during load
$("#success-alert-added").hide();
$("#success-alert-remove").hide();

jQuery(document).ready(function($){
    
    // jQuery sticky Menu
    
	$(".mainmenu-area").sticky({topSpacing:0});
    
    
    $('.product-carousel').owlCarousel({
        loop:true,
        nav:true,
        margin:20,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:3,
            },
            1000:{
                items:5,
            }
        }
    });  
    
    $('.related-products-carousel').owlCarousel({
        loop:true,
        nav:true,
        margin:20,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:2,
            },
            1200:{
                items:3,
            }
        }
    });  
    
    $('.brand-list').owlCarousel({
        loop:true,
        nav:true,
        margin:20,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:3,
            },
            1000:{
                items:4,
            }
        }
    });    
    
    
    // Bootstrap Mobile Menu fix
    $(".navbar-nav li a").click(function(){
        $(".navbar-collapse").removeClass('in');
    });    
    
    // jQuery Scroll effect
    $('.navbar-nav li a, .scroll-to-up').bind('click', function(event) {
        var $anchor = $(this);
        var headerH = $('.header-area').outerHeight();
        $('html, body').stop().animate({
            scrollTop : $($anchor.attr('href')).offset().top - headerH + "px"
        }, 1200, 'easeInOutExpo');

        event.preventDefault();
    });    
    
    // Bootstrap ScrollPSY
    $('body').scrollspy({ 
        target: '.navbar-collapse',
        offset: 95
    });

    //add item
    $('#cart').click(function(e){
        e.preventDefault();
        var pk = $(this).attr('data-pk');
        var quantity = $('#qty').val();
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: 'post',
            url: '/add_cart',
            data:{
                pk: pk,
                quantity: quantity,
                csrfmiddlewaretoken: csrfmiddlewaretoken,
            },
            success: function(){
                $("#success-alert-added").alert();
                $("#success-alert-added").fadeTo(2000, 500).slideUp(500, function(){
                  $("#success-alert-added").slideUp(500);
        });   
            },
        });
    });

    //remove item
    $('.rem-item').click(function(e){
        var pk = $(e.target).attr('data-pk');
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.post('/remove', {'pk':pk, 'csrfmiddlewaretoken':csrfmiddlewaretoken}, function(){
            $("#success-alert-remove").alert();
                $("#success-alert-remove").fadeTo(2000, 500).slideUp(500, function(){
                  $("#success-alert-remove").slideUp(500);
        });   
        });
    });
});

