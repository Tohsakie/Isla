<template>
    <div class="navbar">
      <nav>
        <ul>
          <li><a href="#">Accueil</a></li>
          <li><a href="#">Phase de test</a></li>
          <li><a href="#">Services</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
    </div>
  </template>
  
  <style scoped>
  .navbar {
    margin-top: 2%;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    /* Styles restants */
    top: 0;
    background: rgba(30,30,30,0.8);

    border-radius: 25px;
    padding: 10px 20px;
  }
  
  nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    text-align: center;
  }
  
  nav ul li {
    display: inline;
    margin: 0 10px;
  }
  
  nav ul li a {
    text-decoration: none;
    color: #ffffff99;
    font-weight: bold;
  }
  
  nav ul li:hover {
    background-color: rgba(77, 77, 77, 0.8);
    border-radius: 25px;
  }
  </style>
  