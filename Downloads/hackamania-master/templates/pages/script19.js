/**
 * Created by shyam on 23/3/17.
 */
$(function() {

    $('#clickme').click(function(){

        $.getJSON('http://10.20.3.111:6000/',function(data){

            var item=[]
            $.each(data,function(key,val){

                item.push('<li id="'+ key + '">' + val + '</li>');
            });

            $('<ul/>',{
                'class':'interest-list',
                html:item.join('')

                }).append('body');
            );
        });
    });
});