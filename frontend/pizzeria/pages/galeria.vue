<template>
  <div>
    <ModalGalleryDetail :index="index" v-model="showDetail"/>
    <div v-for="(gallery, index) in galleries" :key="gallery.name + '_' +index">
<!--      <h6>{{ gallery.name }}</h6>-->
      <vue-masonry-wall class="gallery mx-auto" :items="gallery.images"
                        :options="{width: 300, padding: { default: 12, 1: 6, 2: 8}}">
        <template v-slot:default="{item}">
          <!--          <v-img contain :src="'localhost:8000' + item.preview_url" class="gallery-image" justify="space-around" @click="imageClickHandler(item.index)"/>-->
          <v-img contain :src="baseURL + item.preview_url" class="gallery-image scale-on-hover"
                    justify="space-around" loading="lazy" @click="imageClickHandler(item.gallery_index)"/>
        </template>
      </vue-masonry-wall>
    </div>
  </div>
</template>

<script>
import VueMasonryWall from 'vue-masonry-wall'
import ModalGalleryDetail from "../components/GalleryDetail";

export default {
  name: 'galeria',
  components: {
    ModalGalleryDetail,
    VueMasonryWall,
  },
  layout: 'no_footer',
  data() {
    return {
      showDetail: false,
      index: 0,
      baseURL: process.env.baseUrl
    }
  },
  computed: {
    galleries() {
      return this.$store.state.galleries
    },
  },
  methods: {
    imageClickHandler(index) {
      // event.preventDefault();
      this.index = index;
      this.showDetail = true;
    },
  },
  created() {
    if (this.$store.state.galleries.length < 1) {
      this.$store.dispatch('fetchGalleries');
    }
  }
}
</script>

<style lang="scss">
.gallery {
  flex-flow: row wrap;
  width: 100%;

  .masonry-column {
    flex: auto;
    min-width: 300px;
    margin: 0 8px 8px 0;

    .masonry-item {
      width: 100%;
      align-items: stretch;
      justify-content: stretch;

      .gallery-image {
        box-shadow: 6px 6px 5px #0f0f0f;
        filter: grayscale(30%);
        border-radius: 10px;
      }
    }
  }
}
</style>
