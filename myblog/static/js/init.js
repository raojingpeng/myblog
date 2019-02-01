(function ($) {
	$(function () {
		// Render title
		let active_title = $('#slide-out li.active:first-child a').clone();
		active_title.find('i').remove();
		$('.top-nav h3.header').text($.trim(active_title.text()));

		// Initialize components
		$('.sidenav').sidenav();
		$('.collapsible').collapsible();
		$('.tooltipped').map(function () {
			$(this).attr('data-tooltip', moment($(this).data('timestamp')).format('YYYY/MM/DD HH:mm:ss'));
		});
		$('.tooltipped').tooltip();
	});
})(jQuery)