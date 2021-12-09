import { shallowMount } from '@vue/test-utils'
import Home from '../components/Home.vue'

describe('Home', () => {
  it('Home Compnent', () => {
    const wrapper = shallowMount(Home, {
      data() {
        return {
          user: {
            name: "Antônia",
            email: "antonia.pina@g.globo",
            photo:
              "https://www.rd.com/wp-content/uploads/2017/09/01-shutterstock_476340928-Irina-Bg.jpg",
          },
          searchTerms: '',
          cards: [],
          filtered: []
        }
      }
    })
  })
})