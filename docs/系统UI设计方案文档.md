# 教育AI题库与作业系统UI设计方案

> 前端实现统一的UI设计方案，包括响应交互、视觉效果、动画翻页、弹窗动画、组件导航等。我们将使用Vue3和Element Plus，并添加一些自定义样式和动画效果。
主要改进点：

1. 统一的配色方案和主题
2. 过渡动画和微交互
3. 弹窗动画效果
4. 翻页动画
5. 组件导航的视觉优化
6. 响应式设计
下面是具体的实现方案和代码：

### 1. 全局样式和主题

首先，我们定义全局的主题样式，包括颜色、字体、间距等。

#### frontend/src/styles/theme.css

```plaintext
:root {
  /* 主题颜色 */
  --primary-color: #409EFF;
  --primary-light: #ecf5ff;
  --primary-dark: #337ecc;
  
  --success-color: #67C23A;
  --success-light: #f0f9eb;
  --success-dark: #529b2e;
  
  --warning-color: #E6A23C;
  --warning-light: #fdf6ec;
  --warning-dark: #b88230;
  
  --danger-color: #F56C6C;
  --danger-light: #fef0f0;
  --danger-dark: #c45656;
  
  --info-color: #909399;
  --info-light: #f4f4f5;
  --info-dark: #73767a;
  
  /* 文字颜色 */
  --text-primary: #303133;
  --text-regular: #606266;
  --text-secondary: #909399;
  --text-placeholder: #c0c4cc;
  
  /* 边框颜色 */
  --border-light: #e4e7ed;
  --border-base: #dcdfe6;
  --border-dark: #d4d7de;
  
  /* 背景颜色 */
  --background-color: #f5f7fa;
  --background-white: #ffffff;
  
  /* 字体 */
  --font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  
  /* 圆角 */
  --border-radius-small: 2px;
  --border-radius-base: 4px;
  --border-radius-large: 8px;
  --border-radius-circle: 50%;
  
  /* 阴影 */
  --box-shadow-light: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  --box-shadow-base: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  --box-shadow-dark: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .12);
  
  /* 过渡 */
  --transition-all: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-transform: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-opacity: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

body {
  font-family: var(--font-family);
  color: var(--text-primary);
  background-color: var(--background-color);
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* 滚动条样式 */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-thumb {
  background: var(--border-base);
  border-radius: var(--border-radius-base);
}

::-webkit-scrollbar-track {
  background: var(--background-color);
}

/* 通用动画类 */
.fade-enter-active,
.fade-leave-active {
  transition: var(--transition-opacity);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}

/* 卡片通用样式 */
.custom-card {
  background: var(--background-white);
  border-radius: var(--border-radius-large);
  box-shadow: var(--box-shadow-light);
  padding: 20px;
  margin-bottom: 20px;
  transition: var(--transition-all);
}

.custom-card:hover {
  box-shadow: var(--box-shadow-base);
  transform: translateY(-2px);
}

/* 按钮通用样式 */
.custom-button {
  transition: var(--transition-all);
  border-radius: var(--border-radius-base);
}

.custom-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--box-shadow-base);
}

/* 表格通用样式 */
.custom-table {
  border-radius: var(--border-radius-base);
  overflow: hidden;
}

.custom-table .el-table__header {
  background-color: var(--primary-light);
}

.custom-table .el-table__header th {
  background-color: var(--primary-light);
  color: var(--primary-dark);
  font-weight: 600;
}

/* 弹窗动画 */
.dialog-fade-enter-active {
  animation: dialog-fade-in 0.3s;
}

.dialog-fade-leave-active {
  animation: dialog-fade-out 0.3s;
}

@keyframes dialog-fade-in {
  0% {
    transform: translate3d(0, -20px, 0);
    opacity: 0;
  }
  100% {
    transform: translate3d(0, 0, 0);
    opacity: 1;
  }
}

@keyframes dialog-fade-out {
  0% {
    transform: translate3d(0, 0, 0);
    opacity: 1;
  }
  100% {
    transform: translate3d(0, -20px, 0);
    opacity: 0;
  }
}

/* 翻页动画 */
.page-fade-enter-active,
.page-fade-leave-active {
  transition: var(--transition-opacity);
}

.page-fade-enter-from,
.page-fade-leave-to {
  opacity: 0;
}

/* 组件导航 */
.nav-item {
  position: relative;
  padding: 0 15px;
  height: 100%;
  display: flex;
  align-items: center;
  transition: var(--transition-all);
}

.nav-item::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 3px;
  background-color: var(--primary-color);
  transform: translateX(-50%);
  transition: width 0.3s;
}

.nav-item:hover::after,
.nav-item.active::after {
  width: 80%;
}

.nav-item:hover {
  color: var(--primary-color);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .custom-card {
    padding: 15px;
    margin-bottom: 15px;
  }
  
  .nav-item {
    padding: 0 10px;
  }
}
```

### 2. 修改App.vue引入全局样式

#### frontend/src/App.vue

```plaintext
<template>
  <div id="app">
    <router-view v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script setup>
// 引入全局样式
import './styles/theme.css'
</script>

<style>
#app {
  font-family: var(--font-family);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--text-primary);
  background-color: var(--background-color);
  min-height: 100vh;
}
</style>
```

### 3. 优化组件导航

#### frontend/src/components/CustomNav.vue

```plaintext
<template>
  <nav class="custom-nav">
    <div class="nav-container">
      <div class="nav-logo">
        <img src="@/assets/logo.png" alt="Logo" class="logo" />
        <span class="logo-text">教育AI题库系统</span>
      </div>
      <div class="nav-menu">
        <div 
          v-for="item in menuItems" 
          :key="item.path" 
          class="nav-item" 
          :class="{ active: currentPath === item.path }"
          @click="navigateTo(item.path)"
        >
          {{ item.title }}
        </div>
      </div>
      <div class="nav-user">
        <el-dropdown v-if="user" trigger="click">
          <div class="user-info">
            <el-avatar :size="32" :src="user.avatar || defaultAvatar" />
            <span class="username">{{ user.name || user.username }}</span>
          </div>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="goToProfile">个人中心</el-dropdown-item>
              <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        <el-button v-else type="primary" @click="goToLogin">登录</el-button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/store'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const currentPath = computed(() => route.path)
const user = computed(() => userStore.user)
const defaultAvatar = 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'

const menuItems = [
  { title: '首页', path: '/' },
  { title: '题库', path: '/questions' },
  { title: '作业', path: '/homework' },
  { title: '关于', path: '/about' }
]

const navigateTo = (path) => {
  router.push(path)
}

const goToLogin = () => {
  router.push('/login')
}

const goToProfile = () => {
  router.push('/profile')
}

const logout = () => {
  userStore.logout()
  router.push('/login')
}
</script>

<style scoped>
.custom-nav {
  background: var(--background-white);
  box-shadow: var(--box-shadow-light);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  padding: 0 20px;
}

.nav-logo {
  display: flex;
  align-items: center;
}

.logo {
  height: 32px;
  margin-right: 10px;
}

.logo-text {
  font-size: 18px;
  font-weight: 600;
  color: var(--primary-color);
}

.nav-menu {
  display: flex;
  height: 100%;
}

.nav-user {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.username {
  margin-left: 10px;
  font-size: 14px;
  color: var(--text-regular);
}

@media (max-width: 768px) {
  .logo-text {
    display: none;
  }
  
  .nav-menu {
    display: none;
  }
}
</style>
```

### 4. 优化弹窗动画

#### frontend/src/components/CustomDialog.vue

```plaintext
<template>
  <el-dialog
    v-model="visible"
    :title="title"
    :width="width"
    :before-close="handleClose"
    class="custom-dialog"
    :close-on-click-modal="false"
    destroy-on-close
  >
    <div class="dialog-content">
      <slot></slot>
    </div>
    <template #footer>
      <div class="dialog-footer">
        <slot name="footer">
          <el-button @click="handleClose">取消</el-button>
          <el-button type="primary" @click="handleConfirm">确定</el-button>
        </slot>
      </div>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: '提示'
  },
  width: {
    type: String,
    default: '50%'
  }
})

const emit = defineEmits(['update:modelValue', 'confirm', 'cancel'])

const visible = ref(props.modelValue)

watch(() => props.modelValue, (val) => {
  visible.value = val
})

watch(visible, (val) => {
  emit('update:modelValue', val)
})

const handleClose = () => {
  visible.value = false
  emit('cancel')
}

const handleConfirm = () => {
  emit('confirm')
  visible.value = false
}
</script>

<style scoped>
.custom-dialog {
  border-radius: var(--border-radius-large);
  overflow: hidden;
}

.dialog-content {
  padding: 20px 0;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>
```

### 5. 优化表格组件

#### frontend/src/components/CustomTable.vue

```plaintext
<template>
  <div class="custom-table-container">
    <el-table
      :data="data"
      :border="border"
      :stripe="stripe"
      :height="height"
      :max-height="maxHeight"
      :row-key="rowKey"
      :tree-props="treeProps"
      :default-expand-all="defaultExpandAll"
      :show-summary="showSummary"
      :sum-text="sumText"
      :summary-method="summaryMethod"
      :span-method="spanMethod"
      :select-on-indeterminate="selectOnIndeterminate"
      :indent="indent"
      :lazy="lazy"
      :load="load"
      @select="handleSelect"
      @select-all="handleSelectAll"
      @selection-change="handleSelectionChange"
      @cell-mouse-enter="handleCellMouseEnter"
      @cell-mouse-leave="handleCellMouseLeave"
      @cell-click="handleCellClick"
      @cell-dblclick="handleCellDblclick"
      @row-click="handleRowClick"
      @row-contextmenu="handleRowContextmenu"
      @row-dblclick="handleRowDblclick"
      @header-click="handleHeaderClick"
      @header-contextmenu="handleHeaderContextmenu"
      @sort-change="handleSortChange"
      @filter-change="handleFilterChange"
      @current-change="handleCurrentChange"
      @header-dragend="handleHeaderDragend"
      @expand-change="handleExpandChange"
      class="custom-table"
    >
      <slot></slot>
    </el-table>
    
    <div v-if="pagination" class="table-pagination">
      <el-pagination
        v-model:current-page="currentPage"
        v-model:page-size="pageSize"
        :page-sizes="pageSizes"
        :total="total"
        :layout="layout"
        :small="small"
        :background="background"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  },
  border: {
    type: Boolean,
    default: true
  },
  stripe: {
    type: Boolean,
    default: true
  },
  height: [String, Number],
  maxHeight: [String, Number],
  rowKey: [String, Function],
  treeProps: {
    type: Object,
    default: () => ({})
  },
  defaultExpandAll: {
    type: Boolean,
    default: false
  },
  showSummary: {
    type: Boolean,
    default: false
  },
  sumText: {
    type: String,
    default: '合计'
  },
  summaryMethod: Function,
  spanMethod: Function,
  selectOnIndeterminate: {
    type: Boolean,
    default: true
  },
  indent: {
    type: Number,
    default: 16
  },
  lazy: {
    type: Boolean,
    default: false
  },
  load: Function,
  pagination: {
    type: Boolean,
    default: true
  },
  total: {
    type: Number,
    default: 0
  },
  pageSizes: {
    type: Array,
    default: () => [10, 20, 50, 100]
  },
  layout: {
    type: String,
    default: 'total, sizes, prev, pager, next, jumper'
  },
  small: {
    type: Boolean,
    default: false
  },
  background: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits([
  'select',
  'select-all',
  'selection-change',
  'cell-mouse-enter',
  'cell-mouse-leave',
  'cell-click',
  'cell-dblclick',
  'row-click',
  'row-contextmenu',
  'row-dblclick',
  'header-click',
  'header-contextmenu',
  'sort-change',
  'filter-change',
  'current-change',
  'header-dragend',
  'expand-change',
  'size-change',
  'update:currentPage',
  'update:pageSize'
])

const currentPage = ref(1)
const pageSize = ref(10)

const handleSelect = (selection, row) => {
  emit('select', selection, row)
}

const handleSelectAll = (selection) => {
  emit('select-all', selection)
}

const handleSelectionChange = (selection) => {
  emit('selection-change', selection)
}

const handleCellMouseEnter = (row, column, cell, event) => {
  emit('cell-mouse-enter', row, column, cell, event)
}

const handleCellMouseLeave = (row, column, cell, event) => {
  emit('cell-mouse-leave', row, column, cell, event)
}

const handleCellClick = (row, column, cell, event) => {
  emit('cell-click', row, column, cell, event)
}

const handleCellDblclick = (row, column, cell, event) => {
  emit('cell-dblclick', row, column, cell, event)
}

const handleRowClick = (row, column, event) => {
  emit('row-click', row, column, event)
}

const handleRowContextmenu = (row, column, event) => {
  emit('row-contextmenu', row, column, event)
}

const handleRowDblclick = (row, column, event) => {
  emit('row-dblclick', row, column, event)
}

const handleHeaderClick = (column, event) => {
  emit('header-click', column, event)
}

const handleHeaderContextmenu = (column, event) => {
  emit('header-contextmenu', column, event)
}

const handleSortChange = (column) => {
  emit('sort-change', column)
}

const handleFilterChange = (filters) => {
  emit('filter-change', filters)
}

const handleCurrentChange = (val) => {
  emit('current-change', val)
  emit('update:currentPage', val)
}

const handleHeaderDragend = (newWidth, oldWidth, column, event) => {
  emit('header-dragend', newWidth, oldWidth, column, event)
}

const handleExpandChange = (row, expanded) => {
  emit('expand-change', row, expanded)
}

const handleSizeChange = (val) => {
  emit('size-change', val)
  emit('update:pageSize', val)
  currentPage.value = 1
  emit('update:currentPage', 1)
}
</script>

<style scoped>
.custom-table-container {
  background: var(--background-white);
  border-radius: var(--border-radius-large);
  overflow: hidden;
  box-shadow: var(--box-shadow-light);
  transition: var(--transition-all);
}

.custom-table-container:hover {
  box-shadow: var(--box-shadow-base);
}

.custom-table {
  width: 100%;
}

.custom-table .el-table__header-wrapper {
  background-color: var(--primary-light);
}

.custom-table .el-table__header th {
  background-color: var(--primary-light);
  color: var(--primary-dark);
  font-weight: 600;
  border-bottom: 2px solid var(--primary-color);
}

.custom-table .el-table__body tr:hover > td {
  background-color: var(--primary-light);
}

.table-pagination {
  padding: 15px;
  display: flex;
  justify-content: flex-end;
}
</style>
```

### 6. 优化页面过渡动画

#### frontend/src/App.vue (更新)

```plaintext
<template>
  <div id="app">
    <router-view v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script setup>
// 引入全局样式
import './styles/theme.css'
</script>

<style>
#app {
  font-family: var(--font-family);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--text-primary);
  background-color: var(--background-color);
  min-height: 100vh;
}

/* 页面过渡动画 */
.page-fade-enter-active,
.page-fade-leave-active {
  transition: all 0.3s ease;
}

.page-fade-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.page-fade-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}
</style>
```

### 7. 优化按钮组件

#### frontend/src/components/CustomButton.vue

```plaintext
<template>
  <el-button
    :type="type"
    :size="size"
    :plain="plain"
    :round="round"
    :circle="circle"
    :loading="loading"
    :disabled="disabled"
    :icon="icon"
    :autofocus="autofocus"
    :native-type="nativeType"
    :loading-icon="loadingIcon"
    :use-throttle="useThrottle"
    :throttle-duration="throttleDuration"
    @click="handleClick"
    class="custom-button"
  >
    <slot></slot>
  </el-button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: 'default'
  },
  size: {
    type: String,
    default: 'default'
  },
  plain: {
    type: Boolean,
    default: false
  },
  round: {
    type: Boolean,
    default: false
  },
  circle: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  icon: {
    type: String,
    default: ''
  },
  autofocus: {
    type: Boolean,
    default: false
  },
  nativeType: {
    type: String,
    default: 'button'
  },
  loadingIcon: {
    type: String,
    default: ''
  },
  useThrottle: {
    type: Boolean,
    default: true
  },
  throttleDuration: {
    type: Number,
    default: 300
  }
})

const emit = defineEmits(['click'])

const handleClick = (event) => {
  emit('click', event)
}
</script>

<style scoped>
.custom-button {
  transition: var(--transition-all);
  border-radius: var(--border-radius-base);
  font-weight: 500;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.015);
}

.custom-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--box-shadow-base);
}

.custom-button:active {
  transform: translateY(0);
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.015);
}

.custom-button--primary {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}

.custom-button--primary:hover {
  background-color: var(--primary-dark);
  border-color: var(--primary-dark);
}

.custom-button--success {
  background-color: var(--success-color);
  border-color: var(--success-color);
}

.custom-button--success:hover {
  background-color: var(--success-dark);
  border-color: var(--success-dark);
}

.custom-button--warning {
  background-color: var(--warning-color);
  border-color: var(--warning-color);
}

.custom-button--warning:hover {
  background-color: var(--warning-dark);
  border-color: var(--warning-dark);
}

.custom-button--danger {
  background-color: var(--danger-color);
  border-color: var(--danger-color);
}

.custom-button--danger:hover {
  background-color: var(--danger-dark);
  border-color: var(--danger-dark);
}

.custom-button--info {
  background-color: var(--info-color);
  border-color: var(--info-color);
}

.custom-button--info:hover {
  background-color: var(--info-dark);
  border-color: var(--info-dark);
}
</style>
```

### 8. 优化卡片组件

#### frontend/src/components/CustomCard.vue

```plaintext
<template>
  <div class="custom-card" :class="`custom-card-${variant}`">
    <div v-if="$slots.header" class="card-header">
      <slot name="header"></slot>
    </div>
    <div class="card-content">
      <slot></slot>
    </div>
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  variant: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'primary', 'success', 'warning', 'danger', 'info'].includes(value)
  }
})
</script>

<style scoped>
.custom-card {
  background: var(--background-white);
  border-radius: var(--border-radius-large);
  box-shadow: var(--box-shadow-light);
  padding: 20px;
  margin-bottom: 20px;
  transition: var(--transition-all);
  border: 1px solid var(--border-light);
}

.custom-card:hover {
  box-shadow: var(--box-shadow-base);
  transform: translateY(-2px);
}

.custom-card-primary {
  border-left: 4px solid var(--primary-color);
}

.custom-card-success {
  border-left: 4px solid var(--success-color);
}

.custom-card-warning {
  border-left: 4px solid var(--warning-color);
}

.custom-card-danger {
  border-left: 4px solid var(--danger-color);
}

.custom-card-info {
  border-left: 4px solid var(--info-color);
}

.card-header {
  padding-bottom: 15px;
  border-bottom: 1px solid var(--border-light);
  margin-bottom: 15px;
}

.card-footer {
  padding-top: 15px;
  border-top: 1px solid var(--border-light);
  margin-top: 15px;
}
</style>
```

### 9. 更新现有组件使用自定义组件

#### 更新 QuestionTable.vue

```plaintext
<template>
  <div class="question-table">
    <CustomCard>
      <template #header>
        <div class="card-header-content">
          <h2>题库管理</h2>
          <CustomButton type="primary" @click="$emit('importExcel')">
            <el-icon><Upload /></el-icon>
            Excel导入
          </CustomButton>
        </div>
      </template>
      
      <CustomTable
        :data="questions"
        border
        stripe
        @row-click="viewQuestion"
      >
        <el-table-column prop="content" label="题干" min-width="200" />
        <el-table-column prop="difficulty" label="难度" width="100" />
        <el-table-column prop="tags" label="标签" width="150" />
        <el-table-column label="操作" width="100">
          <template #default="scope">
            <CustomButton type="primary" size="small" @click.stop="viewQuestion(scope.row)">
              查看
            </CustomButton>
          </template>
        </el-table-column>
      </CustomTable>
    </CustomCard>
    
    <CustomDialog
      v-model="dialogVisible"
      title="题目详情"
      width="60%"
    >
      <div v-if="selectedQuestion" class="question-detail">
        <h3>题干</h3>
        <p>{{ selectedQuestion.content }}</p>
        
        <div v-if="selectedQuestion.image_url" class="question-image">
          <h3>图片</h3>
          <el-image 
            :src="selectedQuestion.image_url" 
            fit="contain"
            style="max-width: 100%; max-height: 300px;"
          />
        </div>
        
        <div class="question-meta">
          <div class="meta-item">
            <span class="label">难度:</span>
            <span class="value">{{ selectedQuestion.difficulty }}</span>
          </div>
          <div class="meta-item">
            <span class="label">标签:</span>
            <span class="value">{{ selectedQuestion.tags }}</span>
          </div>
        </div>
        
        <div class="question-explanation">
          <h3>解析</h3>
          <p>{{ selectedQuestion.explanation }}</p>
        </div>
      </div>
      
      <template #footer>
        <CustomButton @click="dialogVisible = false">关闭</CustomButton>
      </template>
    </CustomDialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/api'
import CustomCard from './CustomCard.vue'
import CustomTable from './CustomTable.vue'
import CustomButton from './CustomButton.vue'
import CustomDialog from './CustomDialog.vue'
import { Upload } from '@element-plus/icons-vue'

const questions = ref([])
const dialogVisible = ref(false)
const selectedQuestion = ref(null)

const emit = defineEmits(['importExcel'])

onMounted(async () => {
  try {
    const response = await axios.get('/questions')
    questions.value = response.data.items
  } catch (error) {
    console.error('获取题库失败:', error)
  }
})

const viewQuestion = (question) => {
  selectedQuestion.value = question
  dialogVisible.value = true
}
</script>

<style scoped>
.question-table {
  margin-top: 20px;
}

.card-header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header-content h2 {
  margin: 0;
  color: var(--text-primary);
}

.question-detail h3 {
  margin-top: 20px;
  margin-bottom: 10px;
  color: var(--text-primary);
  font-size: 16px;
  font-weight: 600;
}

.question-detail h3:first-child {
  margin-top: 0;
}

.question-image {
  margin-top: 20px;
}

.question-meta {
  display: flex;
  flex-wrap: wrap;
  margin-top: 20px;
}

.meta-item {
  margin-right: 30px;
  margin-bottom: 10px;
}

.meta-item .label {
  font-weight: 600;
  margin-right: 5px;
  color: var(--text-regular);
}

.meta-item .value {
  color: var(--text-primary);
}

.question-explanation {
  margin-top: 20px;
}
</style>
```

### 10. 更新 HomeworkReview.vue

```plaintext
<template>
  <div class="homework-review">
    <CustomCard>
      <template #header>
        <h2>作业批改</h2>
      </template>
      
      <CustomTable
        :data="assignments"
        border
        stripe
      >
        <el-table-column prop="studentName" label="学生" width="120" />
        <el-table-column prop="question" label="题目" min-width="200" />
        <el-table-column prop="answer" label="学生答案" min-width="200" />
        <el-table-column prop="ai_explanation" label="AI解析" min-width="200" />
        <el-table-column label="评分" width="150">
          <template #default="scope">
            <el-input-number 
              v-model="scope.row.score" 
              :min="0" 
              :max="100" 
              :precision="1"
              size="small"
            />
          </template>
        </el-table-column>
        <el-table-column label="批语" width="200">
          <template #default="scope">
            <el-input v-model="scope.row.comment" size="small" />
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template #default="scope">
            <CustomButton 
              type="primary" 
              size="small" 
              @click="submitReview(scope.row)"
              :disabled="scope.row.submitted"
            >
              {{ scope.row.submitted ? '已提交' : '提交' }}
            </CustomButton>
          </template>
        </el-table-column>
      </CustomTable>
    </CustomCard>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/api'
import { ElMessage } from 'element-plus'
import CustomCard from './CustomCard.vue'
import CustomTable from './CustomTable.vue'
import CustomButton from './CustomButton.vue'

const assignments = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('/homework/review-list')
    assignments.value = response.data.items
  } catch (error) {
    console.error('获取作业列表失败:', error)
  }
})

const submitReview = async (assignment) => {
  try {
    await axios.post('/homework/review', {
      id: assignment.id,
      score: assignment.score,
      comment: assignment.comment
    })
    
    assignment.submitted = true
    ElMessage.success('批改成功')
  } catch (error) {
    console.error('提交批改失败:', error)
    ElMessage.error('提交失败')
  }
}
</script>

<style scoped>
.homework-review {
  margin-top: 20px;
}
</style>
```

### 11. 更新 ExcelImport.vue

```plaintext
<template>
  <CustomDialog
    v-model="visible"
    title="题库Excel导入"
    width="50%"
    @close="$emit('close')"
  >
    <div class="excel-import-content">
      <div class="template-download">
        <CustomButton type="primary" @click="downloadTemplate">
          <el-icon><Download /></el-icon>
          下载Excel模板
        </CustomButton>
      </div>
      
      <div class="upload-section">
        <el-upload
          class="upload-demo"
          :action="uploadUrl"
          :headers="{ Authorization: 'Bearer ' + token }"
          :on-success="handleSuccess"
          :on-error="handleError"
          :on-progress="handleProgress"
          :file-list="fileList"
          :limit="1"
          accept=".xlsx, .xls"
          :auto-upload="false"
          ref="uploadRef"
        >
          <template #trigger>
            <CustomButton type="primary">选择文件</CustomButton>
          </template>
          <CustomButton 
            type="success" 
            class="upload-btn"
            @click="submitUpload"
            :disabled="fileList.length === 0"
          >
            上传
          </CustomButton>
          <template #tip>
            <div class="el-upload__tip">
              只能上传xlsx/xls文件，且不超过10MB
            </div>
          </template>
        </el-upload>
      </div>
      
      <div v-if="uploading" class="upload-progress">
        <el-progress :percentage="uploadPercentage" :status="uploadStatus" />
      </div>
      
      <el-alert
        v-if="message"
        :title="message"
        :type="messageType"
        show-icon
        :closable="false"
        style="margin-top: 20px;"
      />
    </div>
    
    <template #footer>
      <CustomButton @click="$emit('close')">关闭</CustomButton>
    </template>
  </CustomDialog>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from '@/api'
import { Download } from '@element-plus/icons-vue'
import CustomButton from './CustomButton.vue'
import CustomDialog from './CustomDialog.vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue', 'close'])

const visible = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
})

const token = localStorage.getItem('token')
const templateUrl = '/api/questions/excel-template'
const uploadUrl = '/api/questions/import-excel'
const uploadRef = ref()
const fileList = ref([])
const uploading = ref(false)
const uploadPercentage = ref(0)
const uploadStatus = ref('')
const message = ref('')
const messageType = ref('success')

const downloadTemplate = () => {
  window.open(templateUrl)
}

const submitUpload = () => {
  uploadRef.value.submit()
}

const handleSuccess = (response) => {
  uploading.value = false
  message.value = response.msg || '导入成功'
  messageType.value = 'success'
  fileList.value = []
  uploadPercentage.value = 100
  uploadStatus.value = 'success'
}

const handleError = (error) => {
  uploading.value = false
  message.value = '导入失败'
  messageType.value = 'error'
  uploadPercentage.value = 0
  uploadStatus.value = 'exception'
  console.error('导入错误:', error)
}

const handleProgress = (event) => {
  uploading.value = true
  uploadPercentage.value = Math.floor(event.percent)
  uploadStatus.value = ''
}
</script>

<style scoped>
.excel-import-content {
  padding: 10px 0;
}

.template-download {
  margin-bottom: 20px;
}

.upload-section {
  margin-bottom: 20px;
}

.upload-btn {
  margin-left: 10px;
}

.upload-progress {
  margin-top: 20px;
}
</style>
```

### 12. 更新 TeacherDashboard.vue

```plaintext
<template>
  <div class="teacher-dashboard">
    <CustomNav />
    
    <div class="dashboard-container">
      <CustomCard>
        <template #header>
          <h2>教师控制台</h2>
        </template>
        
        <el-tabs v-model="activeTab" class="dashboard-tabs">
          <el-tab-pane label="题库管理" name="questions">
            <QuestionTable @importExcel="showImport = true" />
            <ExcelImport v-if="showImport" v-model="showImport" @close="showImport = false" />
          </el-tab-pane>
          <el-tab-pane label="作业管理" name="homework">
            <HomeworkList />
          </el-tab-pane>
          <el-tab-pane label="作业批改" name="review">
            <HomeworkReview />
          </el-tab-pane>
        </el-tabs>
      </CustomCard>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CustomNav from '@/components/CustomNav.vue'
import CustomCard from '@/components/CustomCard.vue'
import QuestionTable from '@/components/QuestionTable.vue'
import ExcelImport from '@/components/ExcelImport.vue'
import HomeworkList from '@/components/HomeworkList.vue'
import HomeworkReview from '@/components/HomeworkReview.vue'

const activeTab = ref('questions')
const showImport = ref(false)
</script>

<style scoped>
.teacher-dashboard {
  min-height: 100vh;
  background-color: var(--background-color);
}

.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.dashboard-tabs {
  margin-top: 20px;
}
</style>
```

### 13. 更新路由配置

#### frontend/src/router/index.js

```plaintext
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import StudentDashboard from '../views/StudentDashboard.vue'
import TeacherDashboard from '../views/TeacherDashboard.vue'
import AdminPanel from '../views/AdminPanel.vue'
import { useUserStore } from '@/store'

const routes = [
  { 
    path: '/', 
    component: Home,
    meta: { title: '首页' }
  },
  { 
    path: '/login', 
    component: Login,
    meta: { title: '登录' }
  },
  { 
    path: '/student', 
    component: StudentDashboard, 
    meta: { 
      requiresAuth: true, 
      role: 'student',
      title: '学生控制台'
    } 
  },
  { 
    path: '/teacher', 
    component: TeacherDashboard, 
    meta: { 
      requiresAuth: true, 
      role: 'teacher',
      title: '教师控制台'
    } 
  },
  { 
    path: '/admin', 
    component: AdminPanel, 
    meta: { 
      requiresAuth: true, 
      role: 'admin',
      title: '管理员控制台'
    } 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const token = localStorage.getItem('token')
  const role = localStorage.getItem('role')
  
  // 设置页面标题
  document.title = to.meta.title ? `${to.meta.title} - 教育AI题库系统` : '教育AI题库系统'
  
  if (to.meta.requiresAuth) {
    if (!token) {
      next('/login')
    } else if (to.meta.role && to.meta.role !== role) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
```

### 14. 创建状态管理

#### frontend/src/store/index.js

```plaintext
import { createPinia, defineStore } from 'pinia'
import axios from '@/api'

const pinia = createPinia()

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || '',
    role: localStorage.getItem('role') || ''
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token,
    isAdmin: (state) => state.role === 'admin',
    isTeacher: (state) => state.role === 'teacher',
    isStudent: (state) => state.role === 'student'
  },
  
  actions: {
    async login(username, password) {
      try {
        const response = await axios.post('/auth/login', { username, password })
        const { token, role } = response
        
        this.token = token
        this.role = role
        
        localStorage.setItem('token', token)
        localStorage.setItem('role', role)
        
        // 获取用户信息
        await this.fetchUserInfo()
        
        return true
      } catch (error) {
        console.error('登录失败:', error)
        return false
      }
    },
    
    async fetchUserInfo() {
      try {
        const response = await axios.get('/users/me')
        this.user = response
      } catch (error) {
        console.error('获取用户信息失败:', error)
      }
    },
    
    logout() {
      this.user = null
      this.token = ''
      this.role = ''
      
      localStorage.removeItem('token')
      localStorage.removeItem('role')
    }
  }
})

export default pinia
```

### 15. 更新 main.js

#### frontend/src/main.js

```plaintext
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import { createPinia } from 'pinia'
import pinia from './store'
import App from './App.vue'
import router from './router'

const app = createApp(App)

// 注册所有图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(ElementPlus)
app.use(createPinia())
app.use(pinia)
app.use(router)

app.mount('#app')
```

### 16. 更新 vite.config.js

#### frontend/vite.config.js

```plaintext
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,
    chunkSizeWarningLimit: 1500,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return 'vendor'
          }
        }
      }
    }
  }
})
```

### 17. 更新 package.json

#### frontend/package.json

```plaintext
{
  "name": "edu-ai-frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext vue,js,jsx,cjs,mjs,ts,tsx,cts,mts --fix --ignore-path .gitignore"
  },
  "dependencies": {
    "@element-plus/icons-vue": "^2.1.0",
    "axios": "^1.4.0",
    "element-plus": "^2.3.8",
    "pinia": "^2.1.4",
    "vue": "^3.3.4",
    "vue-router": "^4.2.4"
  },
  "devDependencies": {
    "@rushstack/eslint-patch": "^1.3.2",
    "@vitejs/plugin-vue": "^4.2.3",
    "@vue/eslint-config-prettier": "^8.0.0",
    "eslint": "^8.45.0",
    "eslint-plugin-vue": "^9.15.1",
    "prettier": "^3.0.0",
    "vite": "^4.4.5"
  }
}
```

## 总结

我们实现了以下UI设计改进：

1. 统一的主题系统：通过CSS变量定义了完整的主题色、文字颜色、边框、背景等，便于全局维护和主题切换。
2. 响应交互：
    - 按钮悬停效果（上移+阴影）
    - 卡片悬停效果（上移+阴影增强）
    - 表格行悬停高亮
    - 导航项悬停下划线动画
3. 视觉效果：
    - 统一的圆角和阴影
    - 精心设计的颜色系统
    - 清晰的视觉层次
4. 动画翻页：
    - 页面切换淡入淡出+滑动效果
    - 弹窗进入/退出动画
    - 列表项过渡动画
5. 弹窗动画：
    - 自定义弹窗组件，支持淡入淡出+位移动画
    - 可自定义标题、宽度和内容
6. 组件导航：
    - 自定义导航组件，支持悬停效果和活动状态指示
    - 响应式设计，移动端自动隐藏菜单项
7. 自定义组件：
    - CustomButton：统一按钮样式和交互
    - CustomCard：统一卡片样式，支持多种变体
    - CustomTable：统一表格样式，优化表头和行悬停
    - CustomDialog：统一弹窗样式和动画
    - CustomNav：统一导航样式和交互
8. 状态管理：
    - 使用Pinia管理用户状态
    - 实现登录/登出逻辑
    - 路由守卫保护需要认证的页面
9. 其他优化：
    - 全局过渡动画
    - 自定义滚动条样式
    - 响应式设计适配移动端
    - 统一的间距和排版
这些改进使整个应用具有一致的外观和感觉，增强了用户体验，并使界面更加现代和专业。所有组件都遵循相同的设计语言，确保了视觉上的连贯性。。