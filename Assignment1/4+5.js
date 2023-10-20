$(document).ready(function(){
    //Modify jquery additional methods to fit canadian specifications
    jQuery.validator.addMethod("zipcodeCDN", function(postal, element) {
        return this.optional(element) || 
        postal.match(/[a-zA-Z][0-9][a-zA-Z](-| |)[0-9][a-zA-Z][0-9]/);
    }, "Please specify a valid postal code.");

    $('form[name="registration"]').validate({
        rules:{
            email:{
                required: true,
                email: true
            },
            password:{
                required: true,
                minlength: 10
            },
            firstname:"required",
            lastname:"required",
            zipcode:{ 
                required: true,
                zipcodeCDN: true,
            },
            phonenumber:{
                required: true,
                phoneUS: true
            }
            
        },
        messages:{
            email:"Please enter a valid email address",
            password:"Please enter a valid password, must be 10 characters long",
            firstname:"Please enter your firstname",
            lastname:"Please enter your lastname",

        },

        submitHandler: function(){
            form.submit();
        }
    })
})

$(document).ready(function(){
    $(".bxslider").bxSlider({
        mode: 'fade',
        captions: true,
    });
})