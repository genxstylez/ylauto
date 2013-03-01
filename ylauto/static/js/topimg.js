jQuery(function($){
	$('#fader1').crossFader();
	$('#fader2').crossFader({
		timer: 3000,
		speed: 1000,
		changeSpd: 400
	});
	$('#fader3').crossFader({
		random: true
	});
	$('#fader4').crossFader({
		loop: false
	});
	$('#fader5').crossFader();
});