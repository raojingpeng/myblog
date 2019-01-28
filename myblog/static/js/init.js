(function($){
  $(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    function render_time() {
        return moment($(this).data('timestamp')).format('lll')
    }

    $('.tooltipped').tooltip();
  });
})(jQuery);