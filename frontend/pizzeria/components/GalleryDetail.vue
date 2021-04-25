<template>
  <v-dialog v-model="show"
            fullscreen
            @keydown.left="previousImageHandler()"
            @keydown.right="nextImageHandler()"
            @keydown.esc="closeImageHandler()"
            color="background darken1"
  >
      <v-card class="card" height="90vh" width="auto">
        <v-img contain class="image" height="100%" :src="image">
          <v-btn id="close" @click="closeImageHandler()">
            <v-icon large color="secondary">
              mdi-close-thick
            </v-icon>
          </v-btn>
          <v-btn id="left" @click="previousImageHandler()">
            <v-icon large color="secondary">
              mdi-arrow-left-thick
            </v-icon>
          </v-btn>
          <v-btn id="right" @click="nextImageHandler()">
            <v-icon large color="secondary">
              mdi-arrow-right-thick
            </v-icon>
          </v-btn>
        </v-img>
      </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "ModalGalleryDetail",
  props: {
    index: Number,
    value: Boolean,
  },
  data() {
    return {
      selected: 0,
    }
  },
  computed: {
    images() {
      var images = []
      this.$store.state.galleries.forEach(gallery => {
        images = [...images, ...gallery.images]
      })

      return images
    },
    image() {
      if (this.images.length > 0) {
        const index = this.images.findIndex(image => {
          return image.gallery_index == this.selected
        });
        console.log('index, image :', this.selected, this.images)
        console.log('index, image :', index, this.images[index])
        return 'http://127.0.0.1:8000' + this.images[index].url
      }
      return ''
    },
    show: {
      get () {
        return this.value
      },
      set (value) {
        this.$emit('input', value)
      }
    },
  },
  methods: {
    nextImageHandler() {
      this.selected++;
      if (this.selected > this.images.length - 1 ) {
        this.selected = 0
      }
    },
    previousImageHandler() {
      if (this.selected === 0 ) {
        this.selected = this.images.length - 1
      } else {
        this.selected--;
      }
    },
    closeImageHandler() {
      this.show=false
    }
  },
  watch: {
    index: function(newVal) {
      this.selected = newVal
    }
  }
}
</script>

<style lang="scss">
.card {
  //background: var(--v-drawer_background-base) !important;
  box-shadow: none;

  #close {
    background: transparent;
    box-shadow: none;
    position: absolute;
    right: 0;
    top: 0;
    z-index: 60;
  }

  #left {
    background: transparent;
    box-shadow: none;
    position: absolute;
    left: 0;
    top: 50%;
    z-index: 60;
  }

  #right {
    background: transparent;
    box-shadow: none;
    position: absolute;
    right: 0;
    top: 50%;
    z-index: 60;
  }
}

</style>
