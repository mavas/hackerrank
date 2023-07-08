cmake_minimum_required(VERSION 3.22.1)

#set(CMAKE_BUILD_TYPE Debug)
#find_package(GMP REQUIRED)

project(hackerrank)

add_executable(find_a_triangle code/find_a_triangle.cc)
add_executable(game code/game.cc)
add_executable(the_answer code/the_answer.cc)
add_executable(dima_and_array code/dima_and_array.cc)
#target_link_libraries(the_answer gmp libgmp)
