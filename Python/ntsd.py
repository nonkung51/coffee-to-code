slogan="Energy = My Coffee ^ 2"
my = [2, 9, 4, 8, 8, 8, 8, 8, 6, 5, 3, 3, 9, 1, 6, 1, 1, 1, 8, 5, 1, 5, 4, 1, 2, 2, 2, 6, 2, 6, 1, 6, 5, 5, 1, 1, 5, 1, 8, 6, 8, 7, 6, 6, 9, 2, 7, 2, 7, 5, 7, 4, 9, 1, 7, 9, 7, 6, 2, 4, 2, 1, 8, 6, 6]
coffee = [64.13657302974646, 30.304015135511886, 84.06396374190311, 61.82131509439119, 62.25752966509352, 61.301508953695425, 61.741396161732524, 58.89927843361071, 37.193189340702325, 75.5221821718626, 97.08587264204131, 52.57375771237966, 54.5078995294362, 171.8865905182833, 38.66522985836241, 133.02631318652712, 167.22739010102381, 155.4445238662334, 32.09750769140807, 76.87002016391045, 133.02631318652712, 72.06386056824877, 81.36645500450416, 91.1756546453054, 64.23783931609157, 124.60537709103889, 92.69304181005174, 66.10975722236469, 113.9254141971843, 44.96850749876703, 168.76907299620981, 65.7723346096214, 69.42045807973324, 50.6596486367602, 50.91168824543142, 171.16074316267733, 75.18643494673756, 101.76443386566841, 58.90988881333931, 66.43166915460327, 59.4316834693415, 19.27618812347059, 69.87608079068735, 68.63551073120483, 33.921477955222805, 119.27908450352895, 37.981198356179185, 36.062445840513924, 64.69268008934904, 75.18643494673756, 38.46334061711972, 83.31116371771553, 54.24123073005545, 168.09818559401526, 64.61976698901262, 56.542019772908716, 59.68967367021823, 65.77106760068087, 70.79548008171143, 80.95369046559891, 113.92321975787026, 106.31556800393817, 56.61161541591973, 40.99796742929256, 41.906642273828936]

def get_energy(my, coffee):
    """ Return Energy by equation Energy = My * Coffee ^ 2 """
    return my * coffee ** 2

energy = ''.join(chr(round(get_energy(my[i], coffee[i]))) for i in range(len(my)))
exec(bytes(energy, 'u16')[2:])