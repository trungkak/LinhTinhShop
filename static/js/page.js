

$(document).ready(function () {
    $('#dropdownid').mouseenter(function() {
        $('.dropdown-menu').show();
    })

    $('#dropdownid').mouseout(function() {
        t = setTimeout(function() {
            $('.dropdown-menu').hide();
        }, 100);

        $('.dropdown-menu').on('mouseenter', function() {
            $('.dropdown-menu').show();
            clearTimeout(t);
        }).on('mouseleave', function() {
            $('.dropdown-menu').hide();
        })
    })
})




