# import sample_data as sample
def mappingMain(data):
    data_1 = {}
    all_pages = []



    def sub_main(data,z):
        sample = data[z][2]
        pg_name = data[z][1][0]
        # print("page name",pg_name)
        pg_name_sp = pg_name.split('.')
        all_pages.append(pg_name_sp[0])

        # print(data[0][1])
        # sample = data[1]

        # list for store postions of shapes and texts
        sorted_list = []
        all_elements = []

        # store x and y seperately
        list_x = []
        list_y = []

        # integrate shapes and texts into one list
        for n in range(0, len(sample[0])):
            all_elements.append(sample[0][n])

        # for n in range(0, len(all_elements)):
        #     print(all_elements[n])

        # seperate x and y values from all elemets to find max x and y
        def seperate_xy():
            for n in range(0, len(all_elements)):
                for m in range(1, len(all_elements[0])):
                    list_x.append(all_elements[n][m][0])
                    list_y.append(all_elements[n][m][1])

        def max_x():
            max = 0
            for n in range(0, len(list_x) - 1):
                if ((list_x[n + 1]) > (list_x[max])):
                    max = n + 1
            return list_x[max]





        def max_y():
            max = 0
            for n in range(0, len(list_y) - 1):
                if ((list_y[n + 1]) > (list_y[max])):
                    max = n + 1
            return list_y[max]

        # call the method of seperate_xy
        seperate_xy()
        # ------------

        # print("after sorted")

        # sorting all elements accoring to the y value
        def swap(one, two):
            temp = all_elements[one]
            all_elements[one] = all_elements[two]
            all_elements[two] = temp

        for n in range(0, len(all_elements)):
            max = n
            for m in range(n + 1, len(all_elements)):
                if ((all_elements[m][1][1]) < (all_elements[max][1][1])):
                    max = m
            swap(n, max)
            sorted_list.append(all_elements[n])

        # sorting all elements according to the x value

        diff_list = []

        for n in range(0, len(sorted_list) - 1):
            diff = sorted_list[n][4][1] - sorted_list[n + 1][1][1]
            diff_list.append(diff)

        adj_row = abs(int(sum(diff_list) / len(diff_list)))

        count3 = 0
        kk = []
        i = 0
        for n in range(i, len(sorted_list)):
            for m in range(n + 1, len(sorted_list)):
                if ((sorted_list[m][2][0] <= max_x()) and ((sorted_list[n][1][1] + ((sorted_list[n][4][1]-sorted_list[n][1][1])/2) >= sorted_list[m][1][1]) and (sorted_list[n][4][1] + ((sorted_list[n][4][1]-sorted_list[n][1][1])/2) >= sorted_list[m][4][1]))):
                    count3 = count3 + 1
                    continue
                else:
                    kk.append(m - 1)
                    i = n
                    break
        kk.append(sorted_list.index(sorted_list[-1]))
        kk = list(dict.fromkeys(kk))


        def swap22(one, two):
            temp = sorted_list[one]
            sorted_list[one] = sorted_list[two]
            sorted_list[two] = temp

        def sort22(x, y):
            for n in range(x, y):
                min = n
                for m in range(n + 1, y + 1):
                    if ((sorted_list[m][1][0]) < (sorted_list[min][1][0])):
                        min = m
                swap22(n, min)

        for n in range(0, len(kk)):
            if (n == 0):
                sort22(0, kk[n])
            if (n != 0):
                sort22(kk[n - 1] + 1, kk[n])

        def correcting(x, y):
            for n in range(x, y):
                for m in range(n + 1, y + 1):
                    sorted_list[m][1][1] = sorted_list[n][1][1]

        for i in range(0, len(kk)):
            if (i == 0):
                correcting(0, kk[i])
            if (i != 0):
                correcting(kk[i - 1] + 1, kk[i])

        # identify relashionship among the elements

        for n in range(0, len(sorted_list)):
            if (sorted_list[n][0][1] == 'RB'):
                for m in range(n + 1, len(sorted_list)):
                    if (len(sorted_list[m][0]) >= 2):
                        if (sorted_list[m][0][1] == 'LBL'):
                            sorted_list.insert(n + 1, sorted_list.pop(m))
                            sorted_list[m][0].append('classified')
                            break
                        else:
                            continue

        for n in range(0, len(sorted_list)):
            if (sorted_list[n][0][1] == 'CB'):
                for m in range(n + 1, len(sorted_list)):
                    if (len(sorted_list[m][0]) >= 2):
                        if (sorted_list[m][0][1] == 'LBL'):
                            sorted_list.insert(n + 1, sorted_list.pop(m))
                            sorted_list[m][0].append('classified')
                            break
                        else:
                            continue

        founded_labels = []
        founded_labels_distance = []

        founded_labels_2 = []
        founded_labels_distance_2 = []

        for n in range(0, len(sorted_list) - 1):
            if (sorted_list[n][0][1] == 'RB'):
                x_of_radio_button = sorted_list[n][1][0]
                x_of_label_of_radioo_button = sorted_list[n + 1][2][0]
                y_of_left_top_of_radio_button = sorted_list[n][1][1]
                y_of_left_bottom_of_radio_button = sorted_list[n][4][1]
                button_height = y_of_left_top_of_radio_button - y_of_left_bottom_of_radio_button
                both_button_label_width = x_of_label_of_radioo_button - x_of_radio_button
                half_of_both_button_label_width = both_button_label_width / 2
                quater_of_both_button_label_width = both_button_label_width / 4
                middle_point = x_of_radio_button + half_of_both_button_label_width
                left_point = middle_point - (quater_of_both_button_label_width + half_of_both_button_label_width)
                right_point = middle_point + quater_of_both_button_label_width + half_of_both_button_label_width

                for m in range(0, len(sorted_list)):
                    if ((sorted_list[m][1][0] > left_point) and (sorted_list[m][2][0] < right_point) and (
                            sorted_list[m][0][1] == 'LBL') and sorted_list[m][4][1] < sorted_list[n][1][1]):
                        founded_labels.append(m)
                        founded_labels_distance.append(sorted_list[n][1][1] - sorted_list[m][4][1])

                if (len(founded_labels_distance) > 0):
                    nearest_top_label = founded_labels[founded_labels_distance.index(min(founded_labels_distance))]

                middle_height_of_radio_button = y_of_left_top_of_radio_button + (button_height / 2)
                upper_point = middle_height_of_radio_button + button_height
                lower_point = middle_height_of_radio_button - button_height

                for m in range(0, len(sorted_list)):
                    if ((sorted_list[m][1][1] > upper_point) and (sorted_list[m][4][1] < lower_point) and (
                            sorted_list[m][0][1] == 'LBL') and (sorted_list[m][1][0] < sorted_list[n][1][0]) and (
                            len(sorted_list[m][0]) == 2)):
                        founded_labels_2.append(m)
                        founded_labels_distance_2.append(sorted_list[n][1][0] - sorted_list[m][2][0])

                if (len(founded_labels_distance) > 0):

                    i = nearest_top_label
                    if (len(founded_labels_2) == 0):
                        for m in range(0, len(sorted_list)):
                            if ((sorted_list[m][0][1] == 'RB') and (
                                    sorted_list[m][1][0] > left_point and sorted_list[m][2][0] < right_point) and
                                    sorted_list[m][1][1] > sorted_list[nearest_top_label][4][1]):
                                sorted_list.insert(i + 1, sorted_list.pop(m))
                                sorted_list.insert(i + 2, sorted_list.pop(m + 1))
                                i = i + 2

                        founded_labels.clear()
                        founded_labels_2.clear()
                        founded_labels_distance.clear()
                        founded_labels_distance_2.clear()

        label_count = 0
        input_count = 0

        for n in range(0, len(sorted_list)):
            if (len(sorted_list[n][0]) == 2):
                if ((sorted_list[n][0][1] == 'TXT') or (sorted_list[n][0][1] == 'PW')):
                    input_count = input_count + 1
                if ((sorted_list[n][0][1] == 'LBL') and (len(sorted_list[n][0]) == 2) and (
                        (sorted_list[n - 1][0][1] != 'RB') and (sorted_list[n + 1][0][1] != 'RB') and (
                        sorted_list[n + 1][0][1] != 'DD') and (sorted_list[n - 1][0][1] != 'CB') and (
                                sorted_list[n + 1][0][1] != 'CB'))):
                    label_count = label_count + 1

                    if (label_count == input_count):
                        top_left_n = sorted_list[n][1][0]
                        top_right_n = sorted_list[n][2][0]
                        top_left_n1 = sorted_list[n - 1][1][0]
                        top_right_n1 = sorted_list[n - 1][2][0]

                        sorted_list[n][1][0] = top_left_n1
                        sorted_list[n][2][0] = top_right_n1
                        sorted_list[n][3][0] = top_right_n1
                        sorted_list[n][4][0] = top_left_n1
                        sorted_list[n - 1][1][0] = top_left_n
                        sorted_list[n - 1][2][0] = top_right_n
                        sorted_list[n - 1][3][0] = top_right_n
                        sorted_list[n - 1][4][0] = top_left_n
                        sorted_list.insert(n - 1, sorted_list.pop(n))
                        sorted_list[n][0].append('classified')

                    if (label_count != input_count):
                        for m in range(n + 1, len(sorted_list)):
                            if (sorted_list[m][0][1] == 'RB'):
                                break
                            if (sorted_list[m][0][1] == 'CB'):
                                break
                            if (sorted_list[m][0][1] == 'DD'):
                                break
                            if ((sorted_list[m][0][1] == 'TXT') or (sorted_list[m][0][1] == 'PW')):
                                sorted_list.insert(n + 1, sorted_list.pop(m))
                                sorted_list[n][0].append('classified')
                                break
                            else:
                                continue

        for n in range(0, len(sorted_list)):
            if (len(sorted_list[n][0]) == 2):
                if (sorted_list[n][0][1] == 'LBL'):
                    for m in range(n + 1, len(sorted_list)):
                        if (sorted_list[m][0][1] == 'RB'):
                            break
                        if (sorted_list[m][0][1] == 'CB'):
                            break
                        if ((sorted_list[m][0][1] == 'TXT') or (sorted_list[m][0][1] == 'PW')):
                            break
                        if (sorted_list[m][0][1] == 'DD'):
                            sorted_list.insert(n + 1, sorted_list.pop(m))
                            sorted_list[n][0].append('classified')
                            break
                        else:
                            continue
        #
            # just for testing
        for m in range(0, len(sorted_list)):
            if (sorted_list[m][0][1] == 'CB'):
                sorted_list[m][0][1] = 'RB'
        # just for testing

        # adding group id

        g_id = 1
        for n in range(0, len(sorted_list)):
            if (sorted_list[n][0][1] == 'IMG'):
                sorted_list[n].append(g_id)
                g_id = g_id + 1
            if (sorted_list[n][0][1] == 'HPL'):
                sorted_list[n].append(g_id)
                g_id = g_id + 1
            if (sorted_list[n][0][1] == 'PRGF'):
                sorted_list[n].append(g_id)
                g_id = g_id + 1
            if (sorted_list[n][0][1] == 'BTN'):
                sorted_list[n].append(g_id)
                g_id = g_id + 1
            if ((sorted_list[n][0][1] == 'CB') and (
                    (sorted_list[n + 1][0][1] == 'LBL') or (sorted_list[n + 1][0][1] == 'PRGF'))):
                sorted_list[n].append(g_id)
                g_id = g_id + 1
            if ((sorted_list[n][0][1] == 'LBL') and (
                    (sorted_list[n + 1][0][1] == 'TXT') or (sorted_list[n + 1][0][1] == 'PW') or (
                    sorted_list[n + 1][0][1] == 'PRGF'))):
                sorted_list[n].append(g_id)
                for m in range(n + 1, len(sorted_list)):
                    if (sorted_list[m][0][1] == 'RB'):
                        break
                    if (sorted_list[m][0][1] == 'DD'):
                        break
                    if (sorted_list[m][0][1] == 'CB'):
                        break
                    if ((sorted_list[m][0][1] == 'TXT') or (sorted_list[m][0][1] == 'PW') or (
                            sorted_list[m][0][1] == 'PRGF')):
                        sorted_list[m].append(g_id)
                        g_id = g_id + 1
                        continue
                    else:
                        break
            if ((sorted_list[n][0][1] == 'LBL') and (sorted_list[n + 1][0][1] == 'DD')):
                sorted_list[n].append(g_id)
                for m in range(n + 1, len(sorted_list)):
                    if ((sorted_list[m][0][1] == 'TXT') or (sorted_list[m][0][1] == 'PW')):
                        g_id = g_id + 1
                        break
                    if (sorted_list[m][0][1] == 'CB'):
                        g_id = g_id + 1
                        break
                    if (sorted_list[m][0][1] == 'RB'):
                        g_id = g_id + 1
                        break
                    if (sorted_list[m][0][1] == 'DD'):
                        sorted_list[m].append(g_id)
                        continue
                    else:
                        g_id = g_id + 1
                        break
            if ((sorted_list[n][0][1] == 'LBL') and (len(sorted_list[n][0]) == 2) and (
                    sorted_list[n + 1][0][1] == 'RB')):
                sorted_list[n].append(g_id)
                for m in range(n + 1, len(sorted_list)):
                    if ((sorted_list[m][0][1] == 'TXT') or (sorted_list[m][0][1] == 'PW')):
                        break
                    if (sorted_list[m][0][1] == 'CB'):
                        break
                    if (sorted_list[m][0][1] == 'DD'):
                        break
                    if (sorted_list[m][0][1] == 'RB'):
                        # g_sub_id = 1
                        for i in range(m, len(sorted_list), 2):
                            if ((sorted_list[i][0][1] == 'RB') and (sorted_list[i + 1][0][1] == 'LBL') and (
                                    len(sorted_list[i + 1][0]) == 3)):
                                sorted_list[i].append(g_id)
                                # sorted_list[i].append(str(g_id)+'.'+str(g_sub_id))
                                # sorted_list[i+1].append(str(g_id) + '.' + str(g_sub_id))
                                # g_sub_id = g_sub_id + 1
                                continue
                            else:
                                break
                    else:
                        g_id = g_id + 1
                        break

        def removing_radio_and_check_box_labels():
            r_c = 0
            for n in range(0, len(sorted_list)):
                if (sorted_list[n][0][1] == 'RB'):
                    r_c = r_c + 1

            c_c = 0
            for n in range(0, len(sorted_list)):
                if (sorted_list[n][0][1] == 'CB'):
                    c_c = c_c + 1

            if (r_c > 0):
                for n in range(0, len(sorted_list) - r_c):
                    if (sorted_list[n][0][1] == 'RB'):
                        sorted_list[n][0][0] = sorted_list[n + 1][0][0]
                        sorted_list.pop(n + 1)

            if (c_c > 0):
                for n in range(0, len(sorted_list) - c_c):
                    if (sorted_list[n][0][1] == 'CB'):
                        sorted_list[n][0][0] = sorted_list[n + 1][0][0]
                        sorted_list.pop(n + 1)

        removing_radio_and_check_box_labels()

        for n in range(0, len(sorted_list)):
            half_width_of_n = (sorted_list[n][2][0] - sorted_list[n][1][0]) / 2
            middle = sorted_list[n][1][0] + half_width_of_n
            left_point_boundary = middle - (sorted_list[n][2][0] - sorted_list[n][1][0])
            right_point_boundary = middle + (sorted_list[n][2][0] - sorted_list[n][1][0])

            quater = (sorted_list[n][4][1] - sorted_list[n][1][1]) / 4
            upper_limit = sorted_list[n][1][1]-quater
            lower_limit = sorted_list[n][1][1]+quater

            item_count = 0
            for i in range(0, len(sorted_list)):
                search_item_width = sorted_list[i][2][0] - sorted_list[i][1][0]
                search_item_width = sorted_list[i][4][1] - sorted_list[i][1][1]
                top_middle = sorted_list[i][1][0]+(search_item_width/2)
                left_middle = sorted_list[i][1][1] + (search_item_width / 2)

                if(top_middle >upper_limit and top_middle < lower_limit):
                    item_count = item_count+1

            if(item_count == 2 ):
                for m in range(0, len(sorted_list)):
                    quater_1 = (sorted_list[n][4][1] - sorted_list[n][1][1]) / 4
                    upper_limit_1 = sorted_list[n][1][1] - quater_1
                    lower_limit_1 = sorted_list[n][1][1] + quater_1

                    item_count_1 = 0
                    for j in range(0, len(sorted_list)):
                        search_item_width_1 = sorted_list[j][2][0] - sorted_list[j][1][0]
                        search_item_width_1 = sorted_list[j][4][1] - sorted_list[j][1][1]
                        top_middle_1 = sorted_list[j][1][0] + (search_item_width_1 / 2)
                        left_middle_1 = sorted_list[j][1][1] + (search_item_width_1 / 2)

                        if (top_middle_1 > upper_limit_1 and top_middle_1 < lower_limit_1):
                            item_count_1 = item_count_1 + 1

                    if (item_count_1 == 2):
                        if ((sorted_list[m][1][0] > left_point_boundary) and (sorted_list[m][2][0] < right_point_boundary)):
                            sorted_list[m][1][0] = sorted_list[n][1][0]
                            sorted_list[m][2][0] = sorted_list[n][2][0]
                            sorted_list[m][3][0] = sorted_list[n][3][0]
                            sorted_list[m][4][0] = sorted_list[n][4][0]

                    if ((item_count_1 == 1) and sorted_list[m][0][1] == 'RB'):
                        if ((sorted_list[m][1][0] > left_point_boundary) and (sorted_list[m][2][0] < right_point_boundary) ):
                            sorted_list[m][1][0] = sorted_list[n][1][0]
                            sorted_list[m][2][0] = sorted_list[n][2][0]
                            sorted_list[m][3][0] = sorted_list[n][3][0]
                            sorted_list[m][4][0] = sorted_list[n][4][0]


                    if ((item_count_1 == 1) and sorted_list[m][0][1] == 'CB'):
                        if ((sorted_list[m][1][0] > left_point_boundary) and (sorted_list[m][2][0] < right_point_boundary)  ):
                            sorted_list[m][1][0] = sorted_list[n][1][0]
                            sorted_list[m][2][0] = sorted_list[n][2][0]
                            sorted_list[m][3][0] = sorted_list[n][3][0]
                            sorted_list[m][4][0] = sorted_list[n][4][0]

        # and (sorted_list[m][1][1] > sorted_list[n][4][1])



        # for n in range(0, len(sorted_list)):
        #     half_width_of_n = (sorted_list[n][2][0] - sorted_list[n][1][0]) / 2
        #     middle = sorted_list[n][1][0] + half_width_of_n
        #     left_pont_boundary = middle - (sorted_list[n][2][0] - sorted_list[n][1][0])
        #     right_pont_boundary = middle + (sorted_list[n][2][0] - sorted_list[n][1][0])
        #
        #     half_height_of_m_1 = (sorted_list[n][4][1] - sorted_list[n][1][1]) / 2
        #     three_quater_height_of_m_1 = ((sorted_list[n][4][1] - sorted_list[n][1][1]) * 2.1) / 4
        #     middel_of_m_1 = sorted_list[n][1][1] + half_height_of_m_1
        #     upper_boundry_1 = middel_of_m_1 - three_quater_height_of_m_1
        #     lower_boundry_1 = middel_of_m_1 + three_quater_height_of_m_1
        #     row_element_count_1 = 0
        #     for i in range(0, len(sorted_list)):
        #         if ((sorted_list[i][1][1] > upper_boundry_1) and (sorted_list[i][4][1] < lower_boundry_1)):
        #             row_element_count_1 = row_element_count_1 + 1
        #
        #     if (row_element_count_1 == 2):
        #         for m in range(n + 1, len(sorted_list)):
        #             half_height_of_m = (sorted_list[m][4][1] - sorted_list[m][1][1]) / 2
        #             three_quater_height_of_m = ((sorted_list[m][4][1] - sorted_list[m][1][1]) * 3) / 4
        #             middel_of_m = sorted_list[m][1][1] + half_height_of_m
        #             upper_boundry = middel_of_m - three_quater_height_of_m
        #             lower_boundry = middel_of_m + three_quater_height_of_m
        #             row_element_count = 0
        #             for i in range(0, len(sorted_list)):
        #                 if ((sorted_list[i][1][1] > upper_boundry) and (sorted_list[i][4][1] < lower_boundry)):
        #                     row_element_count = row_element_count + 1
        #             if (row_element_count == 2):
        #                 if ((sorted_list[m][1][0] > left_pont_boundary) and (sorted_list[m][2][0] < right_pont_boundary) ):
        #                     sorted_list[m][1][0] = sorted_list[n][1][0]
        #                     sorted_list[m][2][0] = sorted_list[n][2][0]
        #                     sorted_list[m][3][0] = sorted_list[n][3][0]
        #                     sorted_list[m][4][0] = sorted_list[n][4][0]
        #
        #             if (row_element_count == 1 and sorted_list[m][0][1] == 'RB'):
        #                 if ((sorted_list[m][1][0] > left_pont_boundary) and (sorted_list[m][2][0] < right_pont_boundary) ):
        #                     sorted_list[m][1][0] = sorted_list[n][1][0]
        #                     sorted_list[m][2][0] = sorted_list[n][2][0]
        #                     sorted_list[m][3][0] = sorted_list[n][3][0]
        #                     sorted_list[m][4][0] = sorted_list[n][4][0]
        #
        #
        #             if (row_element_count == 1 and sorted_list[m][0][1] == 'CB'):
        #                 if ((sorted_list[m][1][0] > left_pont_boundary) and (sorted_list[m][2][0] < right_pont_boundary) ):
        #                     sorted_list[m][1][0] = sorted_list[n][1][0]
        #                     sorted_list[m][2][0] = sorted_list[n][2][0]
        #                     sorted_list[m][3][0] = sorted_list[n][3][0]
        #                     sorted_list[m][4][0] = sorted_list[n][4][0]
        #

        page_width = data[z][0][0]

        increase_ratio = (1366 / page_width) * 100


        for n in range(0, len(sorted_list)):
            sorted_list[n][1][0] = sorted_list[n][1][0] * (increase_ratio / 100)
            sorted_list[n][2][0] = sorted_list[n][2][0] * (increase_ratio / 100)
            sorted_list[n][3][0] = sorted_list[n][3][0] * (increase_ratio / 100)
            sorted_list[n][4][0] = sorted_list[n][4][0] * (increase_ratio / 100)




        for n in range(0, len(sorted_list)):

            if ((sorted_list[n][0][1] == 'PRGF') and (sorted_list[n-1][0][1] != 'LBL')):
                word_list = sorted_list[n][0][0].split()
                word_count =0
                letter_count =0
                width = sorted_list[n][2][0] - sorted_list[n][1][0]
                height = sorted_list[n][4][1] - sorted_list[n][1][1]
                for m in range(0,len(word_list)):
                    word_count = word_count + 1

                for m in range(0,len(word_list)):
                    for i in range(0, len(word_list[m])):
                        letter_count = letter_count + 1



                pixels_of_letter =letter_count*10
                ratio =pixels_of_letter/width
                # print("letter count",letter_count)
                # print("pixels",pixels_of_letter)
                # print("width",width)
                # print("ratio",ratio)
                # print("height", height)

                if(word_count > 10):
                    sorted_list[n][0].append('p1')

                else:
                    if (height >= 135):
                        sorted_list[n][0].append('h1')
                    if (height < 130 and height >= 100):
                        sorted_list[n][0].append('h2')
                    if (height < 120 and height >= 100):
                        sorted_list[n][0].append('h3')
                    if (height < 100 and height >= 85):
                        sorted_list[n][0].append('h4')
                    if (height < 85 and height >= 65):
                        sorted_list[n][0].append('h5')
                    if (height < 65 and height >=50):
                        sorted_list[n][0].append('h6')
                    if (height < 50):
                        sorted_list[n][0].append('p')


                    if(ratio > .2):
                        middle_height_of_item = sorted_list[n][1][1] + ((sorted_list[n][4][1] - sorted_list[n][1][1]) / 2)
                        upper_level = middle_height_of_item - (sorted_list[n][4][1] - sorted_list[n][1][1])
                        lower_level = middle_height_of_item + (sorted_list[n][4][1] - sorted_list[n][1][1])
                        countt = 0
                        for i in range(0, len(sorted_list)):
                            if ((sorted_list[i][1][1] > upper_level) and (sorted_list[i][4][1] < lower_level)):
                                countt = countt + 1


                        if (countt == 1):
                            if (sorted_list[n][1][0] < 460):
                                sorted_list[n][0].append('justify')

                            if (sorted_list[n][1][0] > 460 and sorted_list[n][1][0] < 920):
                                sorted_list[n][0].append('center')

                    else:
                        sorted_list[n][0].append('center')

            else:
                sorted_list[n][0].append('p')
                sorted_list[n][0].append('left')


        # print(sorted_list)

        # creating JSON format

        nb_of_images = 1
        nb_of_paragraphs = 1
        nb_of_labels = 1
        nb_of_texts = 1
        nb_of_passwords = 1
        nb_of_radios = 1
        nb_of_checks = 1
        nb_of_dropdowns = 1
        nb_of_hyperlinks = 1
        nb_of_buttons = 1
        hyper =1

        import json

        data = {}

        for n in range(0, len(sorted_list)):

            top = 0



            if (((sorted_list[n][1][1] / max_y()) * 100) == 0):
                top = str(int(((sorted_list[n][1][1]) / max_y()) * 100)) + '%'
            elif (((sorted_list[n][1][1] / max_y()) * 100) < 10 and ((sorted_list[n][1][1] / max_y()) * 100) > 1):
                top = '0' + str(int(((sorted_list[n][1][1]) / max_y()) * 100)) + '%'
            else:
                top = str(int(((sorted_list[n][1][1]) / max_y()) * 100)) + '%'

            if (sorted_list[n][0][1] == 'IMG'):
                data[sorted_list[n][0][1] + '-' + str(nb_of_images)] = {
                    'type': 'img',
                    'groupId': str(sorted_list[n][5]),
                    'text': ' ',
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_images = nb_of_images + 1

            if (sorted_list[n][0][1] == 'PRGF'):

                data[sorted_list[n][0][1] + '-' + str(nb_of_paragraphs)] = {
                    'type': str(sorted_list[n][0][-2]),
                    'groupId': str(sorted_list[n][5]),
                    'alignment':str(sorted_list[n][0][-1]),
                    'text': sorted_list[n][0][0],
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_paragraphs = nb_of_paragraphs + 1

            if (sorted_list[n][0][1] == 'LBL'):
                data[sorted_list[n][0][1] + '-' + str(nb_of_labels)] = {
                    'type': 'label',
                    # 'groupId': str(sorted_list[n][5]),
                    'groupId' : '',
                    'text': sorted_list[n][0][0],
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_labels = nb_of_labels + 1

            if (sorted_list[n][0][1] == 'TXT'):
                data[sorted_list[n][0][1] + '-' + str(nb_of_texts)] = {
                    'type': 'text',
                    'groupId':str(sorted_list[n][5]),
                    'text': '',
                    'placeholder': 'Type your',
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_texts = nb_of_texts + 1

            if (sorted_list[n][0][1] == 'PW'):
                data[sorted_list[n][0][1] + '-' + str(nb_of_passwords)] = {
                    'type': 'password',
                    'groupId': str(sorted_list[n][5]),
                    'text': '',
                    'placeholder': 'Type your Password',
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_passwords = nb_of_passwords + 1

            if (sorted_list[n][0][1] == 'RB'):

                for nn in range(n-1,n-3,-1):
                    if(sorted_list[nn][0][1] == 'LBL'):
                        r_m_label = sorted_list[nn][0][0]
                        # print("r_m_label",r_m_label)
                        break
                    else:
                        continue

                data[sorted_list[n][0][1] + '-' + str(nb_of_radios)] = {
                    'type': 'radio',
                    'name': r_m_label,
                    'groupId': '',
                    'text': sorted_list[n][0][0],
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_radios = nb_of_radios + 1



            if (sorted_list[n][0][1] == 'CB'):
                data[sorted_list[n][0][1] + '-' + str(nb_of_checks)] = {
                    'type': 'checkbox',
                    'groupId': str(sorted_list[n][5]),
                    'text': sorted_list[n][0][0],
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_checks = nb_of_checks + 1

            if (sorted_list[n][0][1] == 'DD'):

                for nn in range(n-1,n-3,-1):
                    if(sorted_list[nn][0][1] == 'LBL'):
                        d_m_label = sorted_list[nn][0][0]
                        # print("d_m_label",d_m_label)
                        break
                    else:
                        continue

                data[sorted_list[n][0][1] + '-' + str(nb_of_dropdowns)] = {
                    'type': 'dropdown',
                    'groupId': str(sorted_list[n][5]),
                    'text': d_m_label,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'top': top,
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                    'option': {
                        'text': sorted_list[n][0][0],
                        'type': 'option',
                        'values': [sorted_list[n][0][0], 'option2', 'option3,', ]
                    }
                }
                nb_of_dropdowns = nb_of_dropdowns + 1

            if (sorted_list[n][0][1] == 'HPL'):
                data[sorted_list[n][0][1] + '-' + str(nb_of_hyperlinks)] = {
                    'type': 'a',
                    'groupId': str(sorted_list[n][5]),
                    'href': str(hyper)+".html",
                    'text': sorted_list[n][0][0],
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_hyperlinks = nb_of_hyperlinks + 1
                hyper =hyper+1

            if (sorted_list[n][0][1] == 'BTN'):
                data[sorted_list[n][0][1] + '-' + str(nb_of_buttons)] = {
                    'type': 'submit',
                    'groupId': str(sorted_list[n][5]),
                    'text': sorted_list[n][0][0],
                    'top': top,
                    'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'width': str(int(((sorted_list[n][2][0] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                    'height': str(int(((sorted_list[n][4][1] - sorted_list[n][1][1]) / max_y()) * 100)) + '%',
                }
                nb_of_buttons = nb_of_buttons + 1


        return data

    import json

    # print(len(data[1][1][0]))
    for z in range(0,len(data)):
        if(len(data[z][1][0]) >1):
            data_1[all_pages[z]] = sub_main(data, z)
            with open("html_generating/InputFiles/mapping_layouts.json", "w") as outfile:
                json.dump(data_1, outfile, indent=8)

    with open('html_generating/InputFiles/mapping_layouts.json') as json_data:
        loaded_json = json.load(json_data)

    page_list =[]

    for i in range(0, len(loaded_json)+1):
        for key in loaded_json.keys():
            page_list.append(key)
            for z in loaded_json[page_list[i]]:
                rel_name = z.split('-')
                if (rel_name[0] == 'HPL'):
                    for x in loaded_json[page_list[i]][z]:
                        json_text = loaded_json[page_list[i]][z]['text']
                        for pp in range(0, len(all_pages)):
                            if (all_pages[pp] == json_text):
                                for x in loaded_json[page_list[i]][z]:
                                    loaded_json[page_list[i]][z]['href'] = all_pages[pp] + '.html'
                                    with open("html_generating/InputFiles/mapping_layouts.json", "w") as jsonFile:
                                        json.dump(loaded_json, jsonFile, indent=8)
                                    break

from mapping_and_layout.shapes import input_array
shapes = input_array()
mappingMain(shapes)
