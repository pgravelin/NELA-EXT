$(document).ready(function () {
  	$('#data').DataTable({
    	"scrollX": true,
    	"scrollY": "50vh",
		"scrollCollapse": true,
		"language": {
    		"lengthMenu": "Display: _MENU_"
        }
  	});
  	$('.dataTables_length').addClass('bs-select');
});