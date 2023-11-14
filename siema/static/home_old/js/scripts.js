<script>
    $(document).ready(function () {
        // Assuming your links have a class 'article-link' and data attributes for type and level
        $('.article').click(function (event) {
            event.preventDefault();  // Prevent the default link behavior

            // Get the URL, title, type, and level of the clicked link
            var url = $(this).attr('href');
            var title = $(this).text();
            var type = $(this).data('type');  // Assuming the type is stored in a data attribute
            var level = $(this).data('level');  // Assuming the level is stored in a data attribute

            // Send a POST request to the server
            $.ajax({
                type: 'POST',
                url: '/update-user-activity/',  // Replace with the actual URL endpoint
                data: {
                    'url': url,
                    'title': title,
                    'type': type,  // Include the type in the data
                    'level': level,  // Include the level in the data
                },
                success: function (data) {
                    console.log('User activity updated successfully');
                },
                error: function (error) {
                    console.error('Error updating user activity:', error);
                }
            });
        });
    });
</script>
