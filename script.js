
$( document ).ready(function() {

    let module_markup = $('template.module-template').html();



    //add button
    $('#add-module-btn').click(function() {
        $('.modules-wrapper').last().append(module_markup);
    });

    //delete button
    //on function for dynamic objects
    $( "body" ).on( "click", ".delete-module-btn", function() {
        $(this).closest('.module').remove();
    });

});
