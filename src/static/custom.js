
    $(document).ready(function(){ 
        $('.nice-card').hover(
            // trigger when mouse hovers
            function(){
                $(this).animate({
                    marginTop: "-=1%",
                },200);
            },
            // trigger when mouse out
            function(){ 
                $(this).animate({
                    marginTop: "0%"
                },200);
            }
        );
    });

      

      $.extend($.expr[":"], {
        "containsIN": function(elem, i, match, array) {
        return (elem.textContent || elem.innerText || "").toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
        }
        });

    $('.cool-bar').on('keyup',function () {
        console.log(filter);
        $('.card-start').show();
	      var filter = $(this).val(); // get the value of the input, which we filter on
        console.log(filter.toLowerCase());
        $('.card-start').find("article:not(:containsIN(" + filter + "))").parent().css('display','none');
    });  