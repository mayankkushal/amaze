$(window).load(function(){$('.loader').fadeOut("slow");});jQuery(document).ready(function($){$(".mainmenu-area").sticky({topSpacing:0});$('.product-carousel').owlCarousel({loop:true,nav:true,margin:20,responsiveClass:true,responsive:{0:{items:1,},600:{items:3,},1000:{items:5,}}});$('.related-products-carousel').owlCarousel({loop:true,nav:true,margin:20,responsiveClass:true,responsive:{0:{items:1,},600:{items:2,},1000:{items:2,},1200:{items:3,}}});$('.brand-list').owlCarousel({loop:true,nav:true,margin:20,responsiveClass:true,responsive:{0:{items:1,},600:{items:3,},1000:{items:4,}}});$(".navbar-nav li a").click(function(){$(".navbar-collapse").removeClass('in');});$('.navbar-nav li a, .scroll-to-up').bind('click',function(event){var $anchor=$(this);var headerH=$('.header-area').outerHeight();$('html, body').stop().animate({scrollTop:$($anchor.attr('href')).offset().top-headerH+"px"},1200,'easeInOutExpo');event.preventDefault();});$('body').scrollspy({target:'.navbar-collapse',offset:95});$('#cart').click(function(e){var pk=$(this).attr('data-pk');var quantity=$('#qty').val();var csrfmiddlewaretoken=$('input[name=csrfmiddlewaretoken]').val();$.ajax({type:'post',url:'/add_cart',data:{pk:pk,quantity:quantity,csrfmiddlewaretoken:csrfmiddlewaretoken,},success:function(){$("#success-alert-added").alert();$("#success-alert-added").fadeTo(2000,500).slideUp(500,function(){$("#success-alert-added").slideUp(500);});},});});$('.rem-item').click(function(e){var pk=$(e.target).attr('data-pk');var csrfmiddlewaretoken=$('input[name=csrfmiddlewaretoken]').val();$.post('/remove',{'pk':pk,'csrfmiddlewaretoken':csrfmiddlewaretoken},function(){$("#success-alert-remove").alert();$("#success-alert-remove").fadeTo(2000,500).slideUp(500,function(){$("#success-alert-remove").slideUp(500);});});});$('#empty').click(function(e){e.preventDefault();var r=confirm("The cart will be completly emptied.");if(r==true){location.href='/empty_cart';};});$('.like').click(function(event){var id=$(event.target).attr('data-id');$.ajax({type:'get',url:'/like',data:{'id':$(event.target).attr('data-id'),'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),},success:function(data){if(data.like){$(event.target).removeClass('btn-info');$(event.target).addClass('btn-danger');}else{$(event.target).removeClass('btn-danger');$(event.target).addClass('btn-info');}},});});$('.like').each(function(event){var id=$(this).attr('data-id');var lp="#"+"like"+id;$.ajax({type:'get',url:'/like_check',data:{'id':$(this).attr('data-id'),csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),},success:function(d){if(d.lkd){$(lp).removeClass('btn-info');$(lp).addClass('btn-danger');}},});});});
