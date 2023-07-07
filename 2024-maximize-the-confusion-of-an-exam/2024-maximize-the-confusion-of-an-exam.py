class Solution:
	def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

		result = 0
		start = 0
		window = {'T' : 0 , 'F' : 0}

		for index in range(len(answerKey)):

			window[answerKey[index]] = window[answerKey[index]] + 1

			if window['T'] >= window['F'] and window['F'] <= k:
				result = max(result , (window['T'] + window['F']))

			elif window['T'] < window['F'] and window['T'] <= k:
				result = max(result , (window['T'] + window['F']))
			else:

				if answerKey[start] == 'T':
					window['T'] = window['T'] - 1

				elif answerKey[start] == 'F':
					window['F'] = window['F'] - 1

				result = max(result , (window['T'] + window['F']))

				start = start + 1

		return result