$(function() {

    // Init banner slider
	$('.banner__slider').slick({
        dots: false,
        prevArrow: '<button type="button" class="slick-prev"></button>',
        nextArrow: '<button type="button" class="slick-next"></button>',
        fade: true,
        responsive: [
            {
                breakpoint: 576,
                settings: 'unslick'
            }
        ]
    })

    // Init products slider
    $('.products__slider').slick({
        fade: true,
        prevArrow: '<button type="button" class="slick-prev"></button>',
        nextArrow: '<button type="button" class="slick-next"></button>',
    })

    // Invoking nav menu
    $(".burger").on('click', function() {
        $('.nav').addClass('is-visible')
    })

    // Closing nav menu
    $(".nav__close").on('click', function() {
        $('.nav').removeClass('is-visible')
    })
   
   

    // Add class to links
    $('.header__links .nav a').on('click', function() {
        $('.header__links .nav a').removeClass('active-link')
        $(this).addClass('active-link')
    })

    

    // if ($(window).width() < 991) {
    //     var text = $("[data-alt]"),
    //         oldText = $("[data-alt]").text()
    //     text.text(text.data().alt)
    // } else {
    //     text.text(oldText)
    // }

    // In mobile devices, all banners except first removed
    if ($(window).width() < 576) {
         $('.banner__slide:not(:first-child)').remove()
    }

    
    // Custom select plugin whic is placed in products section
    let select = function() {
        let selectHeader = document.querySelectorAll('.select__header')
        let selectItem = document.querySelectorAll('.select__item')

        selectHeader.forEach(item => {
            item.addEventListener('click', selectToggle)
        })

        selectItem.forEach(item => {
            item.addEventListener('click', selectChoose)
            
        })

        function selectToggle() {
            this.parentElement.classList.toggle('is-active')
        }

        function countSliders() {
             // Count sliders
             var count = 1
             var length = $(".products__slider_active .slick-slide").length
             var start = $('.sliders-count .start')
             start.text(count)
             
             $('.products .slick-next').on('click', function() {
                 count++
                 start.text(count)
                 if (count > length) {
                     count = 1
                     start.text(count)
                 }
             })

             $('.products .slick-prev').on('click', function() {
                 count--
                 start.text(count)
                 if (count < 1) {
                     count = length
                     start.text(count)
                 }
             })
           

             var end = $('.sliders-count .end')
             end.text(`/${length}`)
        }
        countSliders()

        function selectChoose() {
            let text = this.innerText,
                id = this.dataset.type,
                select = this.closest('.select'),  
                currentText = this.closest('.select').querySelector('.select__current')

                let targets = document.querySelectorAll('.products__slider')
                targets.forEach((target, index) => {
                   let targetId = target.dataset.type
                   target.classList.remove('products__slider_active')
                   if (id === targetId) {
                    target.classList.add('products__slider_active')
                    $('.products__slider').slick('reinit')
                   }
                   countSliders()
                })

            currentText.innerText = text
            select.classList.remove('is-active')
        }
    }
    

    select()
    

    var selectItems = document.querySelectorAll('.select')
    selectItems.forEach(item => {
        if (!item.dataset.da) {
            item.remove()
        }
    })

    // Init parallax
    var scenes = document.querySelectorAll('[data-id]');
    scenes.forEach(scene => {
        var parallaxInstance = new Parallax(scene);
    })

    // 

    function scrollElements() {
        var aboutBlock = document.querySelector('.about').getBoundingClientRect().top
        var productsBlock = document.querySelector('.products').getBoundingClientRect().top
        var contactsBlock = document.querySelector('.contact').getBoundingClientRect().top
      
        if($(window).scrollTop()) {
            $('.header').addClass('header-animate');
            if (aboutBlock < 160  && productsBlock > 250) {
                $('.header__links .nav a').removeClass('active-link')
                $('.header__links .nav li:first-child a').addClass('active-link')
            }
            else if(productsBlock < 250 && contactsBlock > 250) {
                $('.header__links .nav a').removeClass('active-link')
                $('.header__links .nav li:nth-child(2) a').addClass('active-link')
            } 
            else if (contactsBlock < 250) {
                $('.header__links .nav a').removeClass('active-link')
                $('.header__links .nav li:last-child a').addClass('active-link')
            }
        }
        else {
            $('.header__links .nav a').removeClass('active-link')
            $('.header').removeClass('header-animate');
        }
    }

    $(window).on('scroll', scrollElements)
    scrollElements()

    // Init Aos
    AOS.init()

});