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
      font-family: "OleoScript", sans-serif;
      opacity: 0.9;
      font-weight: 500;

      @media (max-width: 600px) {
        font-size: 2rem;
        font-weight: 600;
        letter-spacing: normal;
      }
      @media (min-width: 600px) {
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: 0.5rem;
      }
      @media (min-width: 960px) {
        font-size: 3rem;
        letter-spacing: 0.6rem;
      }
      @media (min-width: 1264px) {
        font-size: 4rem;
        letter-spacing: 0.8rem;
      }

    }
  }
</style>
