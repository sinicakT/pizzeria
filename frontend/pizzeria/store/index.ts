import axios from 'axios'

export const state = () => ({
  menu: {
    loaded: false,
    pizzas: [],
    ingredients: [],
    ingredients_list: [],
    offer: []
  },
  gallery: []
});

export const mutations = {
  setPizzas(state:any, pizzas:any) {
    state.menu.pizzas = pizzas
  },
  setIngredients(state:any, ingredients:any) {
    state.offer.ingredients = ingredients
  },
  setOffer(state:any, menu:any) {
    state.menu.offer = menu
  },
  setCompleteMenu(state:any, data:any) {
    state.menu = {
      pizzas: data['pizzas'],
      ingredients: data['ingredients'],
      ingredients_list: data['ingredients_list'],
      offer: data['offer']

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
        vuexContext.commit('setCompleteMenu', {
          'loaded': true,
          'pizzas': pizzas,
          'ingredients': res.data.ingredients,
          'ingredients_list': res.data.ingredients_list,
          'offer': res.data.offer
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
  setOffer(vuexContext:any, menu:any) {
    vuexContext.commit('setPizzas', menu)
  },
  setCompleteMenu(vuexContext:any, data:any) {
    vuexContext.commit('setCompleteMenu', data)
  }
}

export const getters = () => ({
  pizzas(state:any) {
    return state.menu.pizzas
  },
  ingredients(state:any) {
    return state.offer.ingredients
  },
  offer(state:any) {
    return state.menu.offer
  },
  menu(state:any) {
    return state.menu
  },
  gallery(state:any) {
    return state.gallery
  }
})
