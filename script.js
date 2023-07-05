$(document).ready(function() {
  // Get news articles from News API
  var apiKey = "f7d54802ae9d4e2eb6b90d6e456b63ee";
  var apiUrl = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f7d54802ae9d4e2eb6b90d6e456b63ee";

  $.get(apiUrl, function(data) {
    var articles = data.articles;

    // Display articles in the newsContainer
    var newsContainer = $("#newsContainer");

    for (var i = 0; i < articles.length; i++) {
      var article = articles[i];
      var articleElement = $("<div>").addClass("article");
      var imageElement = $("<img>").attr("src", article.urlToImage).appendTo(articleElement);
      var headingElement = $("<h3>").text(article.title).appendTo(articleElement);
      var paragraphElement = $("<p>").text(article.description).appendTo(articleElement);

      articleElement.appendTo(newsContainer);
    }
  });
});
