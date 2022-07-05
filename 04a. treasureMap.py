# --------------------------------------------------------------
# ---------------------- TREASURE MAP --------------------------
# ----------------- (RANDOMISATION & LISTS) --------------------
# --------------------------------------------------------------

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
row = int(position[0])
column = int(position[1])
map[row-1][column-1] = "x"

print(f"{row1}\n{row2}\n{row3}")


# -------- OLD STEPS ----------
#if row == 1:
#    row1[column-1] = "x"
#elif row == 2:
#    row2[column-1] = "x"
#elif row == 3:
#    row3[column-1] = "x"   
# ------------------ OR ----------------------
#selected_row = map[row-1]
#selected_row[column-1] = "x"