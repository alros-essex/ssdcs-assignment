import { CoreMenu } from '@core/types'

export const menu: CoreMenu[] = [
  {
    id: 'home',
    title: 'Home',
    translate: 'MENU.HOME',
    type: 'item',
    icon: 'home',
    url: 'home'
  },
  {
    id: 'experiments',
    title: 'experiments',
    translate: 'MENU.Experiments',
    type: 'item',
    icon: 'file',
    url: 'sample'
  },
  {
    id: 'users',
    title: 'users',
    translate: 'MENU.Users',
    type: 'item',
    icon: 'user',
    url: 'sample'
  }
]
