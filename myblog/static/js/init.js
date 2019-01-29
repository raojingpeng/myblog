(function($){
  $(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.tooltipped').map(function () {
        $(this).attr('data-tooltip', moment($(this).data('timestamp')).format('YYYY/MM/DD HH:mm:ss'));
      });
    $('.tooltipped').tooltip();
  });
})(jQuery);