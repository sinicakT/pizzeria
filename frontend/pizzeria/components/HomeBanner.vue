<template>
  <div class="home-banner">
    <div class="banner-title">Pre radosť z chuti</div>
  </div>
</template>

<script>
export default {
  name: "HomeBanner"
}
</script>

<style scoped lang="scss">
  .home-banner {
    background-image: url("~/assets/images/home.jpg");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;
    height: 85vh;
    position: relative;
    filter: grayscale(30%);
    box-shadow: 6px 6px 5px #0f0f0f;
    border-radius: 20px;

    -webkit-mask-image: -webkit-gradient(radial, left top, left bottom,
      from(rgba(0,0,0,1)), to(rgba(0,0,0,0)));

    .banner-title {
      position: absolute;
      top: 10%;
      left: 5%;
      font-size: 4rem;
      font-weight: 500;
      font-family: "OleoScript", sans-serif;
      letter-spacing: 0.8rem;
      opacity: 0.9;
    }
  }
</style>
