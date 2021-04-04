import axios from 'axios'

export const state = () => ({
  offer: {
    loaded: false,
    pizzas: [],
    ingredients: [],
    ingredients_list: [],
    menu: []
  },
  gallery: []
});

export const mutations = {
  setPizzas(state:any, pizzas:any) {
    state.offer.pizzas = pizzas
  },
  setIngredients(state:any, ingredients:any) {
    state.offer.ingredients = ingredients
  },
  setmenu(state:any, menu:any) {
    state.offer.menu = menu
  },
  setCompleteOffer(state:any, data:any) {
    state.offer = {
      pizzas: data['pizzas'],
      ingredients: data['ingredients'],
      ingredients_list: data['ingredients_list'],
      menu: data['menu']

    }
  },
  setGallery(state: any, data: any) {
    data.forEach((image: any, index: number) => {
      image.index = index
    })
    state.gallery = data

  }
};

export const actions = {
  // nuxtServerInit(vuexContext:any, context:any) {
  //   return axios.get('http://127.0.0.1:8000/api/pizza/')
  //     .then(res => {
  //       console.log(res);
  //       vuexContext.commit('setCompleteOffer', {
  //         'loaded': true,
  //         'pizzas': res.data,
  //         'ingredients': [],
  //         'menu': []
  //       });
  //     })
  //     .catch(e => context.error(e))
  // },
  fetchAllData(vuexContext: any) {
    return axios.get('http://127.0.0.1:8000/api/menu/')
      .then(res => {
        const pizzas: any[] = [];
        res.data.pizza.forEach((pizza: any) => {
          const ingredients_array: string[] = [];
          pizza.ingredients.forEach((ingredient: any) => {
            ingredients_array.push(ingredient.name)
          })
          pizzas.push({
            ...pizza,
            'ingredients_arr': ingredients_array
          })
        })
        vuexContext.commit('setCompleteOffer', {
          'loaded': true,
          'pizzas': pizzas,
          'ingredients': [],
          'ingredients_list': res.data.ingredients_list,
          'menu': res.data.menu
        });
      })
      .catch(e => console.log(e))
  },
  fetchGallery(vuexContext:any, images:any) {
    images = [
      {
        'preview_url': require('@/assets/images/pizzeria/pizza1.jpg'),
        'detail_url': require('@/assets/images/pizzeria/pizza1.jpg')
      },
      {
        'preview_url': require('@/assets/images/pizzeria/pizza2.jpg'),
        'detail_url': require('@/assets/images/pizzeria/pizza2.jpg')
      },
      {
        'preview_url': require('@/assets/images/pizzeria/pizza3.jpg'),
        'detail_url': require('@/assets/images/pizzeria/pizza3.jpg')
      },
      {
        'preview_url': require('@/assets/images/pizzeria/pizza4.jpg'),
        'detail_url': require('@/assets/images/pizzeria/pizza4.jpg')
      },
      {
        'preview_url': require('@/assets/images/pizzeria/pizza5.jpg'),
        'detail_url': require('@/assets/images/pizzeria/pizza5.jpg')
      },
      {
        'preview_url': require('@/assets/images/pizzeria/pizza6.jpg'),
        'detail_url': require('@/assets/images/pizzeria/pizza6.jpg')
      },
      {
        'preview_url': require('@/assets/images/pizzeria/pizza7.jpg'),
        'detail_url': require('@/assets/images/pizzeria/pizza7.jpg')
      },
    ];

    vuexContext.commit('setGallery', images)
  },
  setPizzas(vuexContext:any, pizzas:any) {
    vuexContext.commit('setPizzas', pizzas)
  },
  setIngredients(vuexContext:any, ingredients:any) {
    vuexContext.commit('setPizzas', ingredients)
  },
  setmenu(vuexContext:any, menu:any) {
    vuexContext.commit('setPizzas', menu)
  },
  setCompleteOffer(vuexContext:any, data:any) {
    vuexContext.commit('setCompleteOfferPizzas', data)
  }
}

export const getters = () => ({
  pizzas(state:any) {
    return state.offer.pizzas
  },
  ingredients(state:any) {
    return state.offer.ingredients
  },
  menu(state:any) {
    return state.offer.menu
  },
  completeOffer(state:any) {
    return state.offer
  },
  gallery(state:any) {
    return state.gallery
  }
})
