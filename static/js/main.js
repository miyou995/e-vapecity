(function($) {
	"use strict"
	// Mobile Nav toggle
	$('.menu-toggle > a').on('click', function (e) {
		e.preventDefault();
		$('#responsive-nav').toggleClass('active');
		
	})
	$(window).on('load', function() {
		$('#myModal').modal('show');
	});

	var qte = '#product_quantity'
	$(qte).on('change', function (e){
		// quantity = document.getElementById("product_quantity")
		var the_num = $(qte)[0].value
		var hidqte = document.getElementById('hiddenQte') 
		hidqte.value = the_num
		console.log('quantity value', hidqte.value );
	})

    $("#wilayaId").change(function () {
        const url = $("#order_form").attr("data-communes-url"); 
        const wilayaPk = $(this).val();
		// var wilaya = $('#wilayaId')
		var wilaya = document.getElementById('wilayaId');
		var selected = wilaya.options[wilaya.selectedIndex];
		var price = selected.getAttribute('data-price');
		console.log('la wilaya a ');
        $.ajax({                   
            url: url,                
            data: {
                'wilaya_id': wilayaPk      
            },
            success: function (data) { 
                $("#communesId").html(data);
                $('#deliveryCost').html(price)
			}
        });
    });

	var alterClass = function() {
		var ww = document.body.clientWidth;
		if (ww > 991) {
		  $('#collapseFilters').removeClass('collapse');
		} else {
			$('#collapseFilters').addClass('collapse');
		};
	  };
	  $(window).resize(function(){
		alterClass();
	  });
	  alterClass();
	$('.cart-dropdown').on('click', function (e) {
		e.stopPropagation();
	});
	/////////////////////////////////////////
	// Products Slick
	$('.products-slick').each(function() {
		var $this = $(this), $nav = $this.attr('data-nav');
		$this.slick({
			slidesToShow: 4,
			slidesToScroll: 1,
			autoplay: true,
			infinite: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
			responsive: [{
	        breakpoint: 991,
	        settings: {
	          slidesToShow: 2,
	          slidesToScroll: 1,
	        }
	      },
	      {
	        breakpoint: 480,
	        settings: {
	          slidesToShow: 1,
	          slidesToScroll: 1,
	        }
	      },
	    ]
		});
	});

	// Products Widget Slick
	$('.products-widget-slick').each(function() {
		var $this = $(this),
				$nav = $this.attr('data-nav');

		$this.slick({
			infinite: true,
			autoplay: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
		});
	});

	/////////////////////////////////////////

	// Product Main img Slick
	$('#product-main-img').slick({
    infinite: true,
    speed: 300,
    dots: false,
    arrows: true,
    fade: true,
    asNavFor: '#product-imgs',
  });

	// Product imgs Slick
  $('#product-imgs').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    centerMode: true,
    focusOnSelect: true,
		centerPadding: 0,
		vertical: true,
    asNavFor: '#product-main-img',
		responsive: [{
        breakpoint: 991,
        settings: {
			vertical: false,
			arrows: false,
			dots: true,
        }
      },
    ]
  });
	// Product img zoom
	var zoomMainProduct = document.getElementById('product-main-img');
	if (zoomMainProduct) {
		$('#product-main-img .product-preview').zoom();
	}
	/////////////////////////////////////////
	// Input number
	$('.input-number').each(function() {
		var $this = $(this),
		$input = $this.find('input[type="number"]'),
		up = $this.find('.qty-up'),
		down = $this.find('.qty-down');

		down.on('click', function () {
			var value = parseInt($input.val()) - 1;
			value = value < 1 ? 1 : value;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})

		up.on('click', function () {
			var value = parseInt($input.val()) + 1;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})
	});

	var priceInputMax = document.getElementById('price-max'),
			priceInputMin = document.getElementById('price-min');

	priceInputMax.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	priceInputMin.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	function updatePriceSlider(elem , value) {
		if ( elem.hasClass('price-min') ) {
			console.log('min')
			priceSlider.noUiSlider.set([value, null]);
		} else if ( elem.hasClass('price-max')) {
			console.log('max')
			priceSlider.noUiSlider.set([null, value]);
		}
	}

	// Price Slider
	var priceSlider = document.getElementById('price-slider');
	if (priceSlider) {
		noUiSlider.create(priceSlider, {
			start: [1, 99999],
			connect: true,
			step: 1,
			range: {
				'min': 1,
				'max': 99999
			}
		});
		priceSlider.noUiSlider.on('update', function( values, handle ) {
			var value = values[handle];
			handle ? priceInputMax.value = value : priceInputMin.value = value
		});
	}
	$('.the-slider').on('click', function (e) {
		alert('defbtbhtrtr');
	});




})(jQuery);
