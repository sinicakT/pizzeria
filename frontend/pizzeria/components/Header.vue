<template>
  <nav id="navigation">
    <v-app-bar fixed outlined :inverted-scroll="invertedScroll" scroll-threshold="50">
      <v-toolbar-title id="logo">
        <router-link to="/" tag="span" style="cursor:pointer">
          <v-img
            class="mr-3"
            :src="require('../assets/logo_line.svg')"
            height="55"
            width="160"
          ></v-img>
        </router-link>
      </v-toolbar-title>
      <div class="hidden-md-and-down ml-md-4 ml-lg-8 menu-box">
        <v-list nav>
                <span v-for="item in menuItems" :key="item.title" class="mx-lg-2">
                  <v-btn text class="secondary--text text--lighten-1 font-default" router :to="item.link"> {{
                      item.title
                    }} </v-btn>
                </span>
        </v-list>
      </div>
      <v-spacer></v-spacer>
      <tasty-burger-button
        type="collapse"
        id="hamburger"
        @toggle="showDrawer = !showDrawer"
        ref="hamburger"
        color="var(--v-secondary-base)"
        active-color="var(--v-secondary-base)"
        class="hidden-lg-and-up"
      ></tasty-burger-button>
    </v-app-bar>
    <v-navigation-drawer v-model="menu"
                         fixed
                         floating
                         disable-route-watcher
                         width="100%"
    >
      <v-layout class="manual-v-layout">
        <v-flex mx-auto
                v-for="(item, index) in menuItems"
                :key="item.title"
        >
          <transition :name="index%2==0 ? 'slide-left' : 'slide-right'"
                      type="animation"
          >
            <v-btn text
                   @click="changeRoute()"
                   router
                   :to="item.link"
                   my-auto
                   class="secondary--text text--lighten-1 font-default"
                   v-show="item.inDrawer"
                   :style="{
                          delay: (index * 0.1).toString() + 's',
                          transitionDelay: (index * drawerItemDelay / 1000).toString() + 's',
                          animationDelay: (index * drawerItemDelay / 1000).toString() + 's',
                          transitionDuration: '0.3s',
                          animationDuration: (drawerItemDuration/1000).toString() + 's'
                        }"
            > {{ item.title }}
            </v-btn>
          </transition>
        </v-flex>
      </v-layout>
    </v-navigation-drawer>
  </nav>
</template>

<script >
import { TastyBurgerButton } from 'vue-tasty-burgers'
import {MENU_ITEMS} from "~/assets/data/data";

export default {
  name: "Header",
  data() {
    return {
      menu: false,
      showDrawer: false,
      drawerItemDelay: 100,
      drawerItemDuration: 500,
      menuItems: MENU_ITEMS
    }
  },
  components: {
    'tasty-burger-button': TastyBurgerButton
  },
  computed: {
    invertedScroll() {
      return !!(this.$route.name === 'home' & !this.menu)
    }
  },
  watch: {
    showDrawer: function (val) {
      if (val) {
        this.showDrawerMenu();
      } else {
        this.hideDrawerMenu();
      }
    }
  },
  methods: {
    changeRoute: function () {
      const test = this.$refs.hamburger.$children[0].$children[0];
      test.toggle();
    },

    showDrawerMenu: function() {
      this.menu = true;
      this.menuItems.forEach(value => {
        // const delay = 500 + ((index + 1) * 150);
        // const delay = 200;
        setTimeout(function() {
          value.inDrawer = true;
        }.bind(this), this.drawerItemDelay)
      })
    },
    hideDrawerMenu: function() {
      this.menuItems.forEach(value => {
        value.inDrawer = false;
      });
      this.menu = false;
      // this.hamburger = false;
      // const test = this.$refs.hamburger.$attrs;
      // this.$refs.hamburger.value = false;
    },
    scrollToTop() {
      window.scrollTo(0, 0)
    }
  }
}
</script>

<style lang="scss">

#navigation {
  z-index: 999;
}

.v-sheet {
  background: $navbar-background !important;
  z-index: 60 !important;

  .v-list--nav {
    background: none !important;
  }
}

.v-navigation-drawer {
  background: $drawer-background !important;
}

.manual-v-layout {
  padding-top: 18vh;
  max-height: 600px;
  height: 100vh;
  display: -webkit-box;
  display: -ms-flex;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
</style>
