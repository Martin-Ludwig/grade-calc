
$( document ).ready(function() {

    let module_markup = $('.modules-wrapper').html();

    $('#add-module-btn').click(function() {
        $('.module').last().append(module_markup);
    });

});
