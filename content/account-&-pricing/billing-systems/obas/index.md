---
draft: false
title: "OBAS Billing System"
aliases: ["/obas/", "/pbas/"]
seoindex: "index, follow"
seotitle: "Billing via OBAS"
seokeywords: "dashboard, account, billing, payment, obas"
seodesc: "This step-by-step instruction shows you how to convert and refill your account if your hosting provider uses oBAS (Odin Business Automation Standard) system."
menu: 
    docs:
        title: "OBAS Billing System"
        url: "/obas/"
        weight: 30
        parent: "billing-systems"
        identifier: "obas.md"
---

# Billing via OBAS

This step-by-step instruction shows you how to convert and refill your account if your hosting provider uses **OBAS (Odin Business Automation Standard)** system.

At the moment OBAS system is used by **[Layershift](https://www.virtuozzo.com/application-platform-partners/layershift/)**, **[Cloudplatform](https://www.virtuozzo.com/application-platform-partners/cloudplatform/)**, **[Elastx](https://www.virtuozzo.com/application-platform-partners/elastx/)**, **[DOCKTERA](https://www.virtuozzo.com/application-platform-partners/docktera/)** and **[Axarnet](https://www.virtuozzo.com/application-platform-partners/axarnet/)**.

* [Conversion](#conversion)<a id="conversion"></a>
* [Refilling](#refilling)


## Conversion

1\. At the dashboard click the button **Upgrade trial account** in the drop-down menu.

![upgrade trial account button](01-upgrade-trial-account-button.png)

2\. Fill out the required fields in the opened window and confirm your agreement with *Terms of service*. Click **Next**.

![OBAS trial to paid conversion](02-obas-trial-to-paid-conversion.png)

3\. Select the payment method (*Credit/Debit card* or *Paypal*) and state the sum using the slider. Click **Next** and then confirm your choice.

{{%tip%}}**Note:** Some hosters provide the additional payment methods alternative to the given by default. In this case you'll be offered to contact the hoster to be able to use some other ways of funding.{{%/tip%}}

![OBAS first refill](03-obas-first-refill.png)

### Card Payment Method

Enter your card details and click **Proceed**.

![enter card derails](04-enter-card-derails.png)

After that **Purchase Authentication** window will be opened. Enter the password for full authentication.

### PayPal Payment Method

* ***with PayPal account***

Click **Log In** button and state your email and password of your PayPal account to make the purchase.

![log in OBAS account](05-log-in-obas-account.png)

![OBAS account credentials](06-obas-account-credentials.png)

After conversion you'll get emails with information about the state of your account converting and refilling. Also such information will appear in the message at the dashboard.

{{%tip%}}**Tip:** If you would like to use auto-refill option in the platform dashboard, you should tick the "*I'd like to use PayPal for future payments to {hoster's name}*" line as it is shown below:

![PayPal auto-refill](07-paypal-auto-refill.png){{%/tip%}}

* ***without PayPal account***

You can use PayPal payment method even if you don't have the PayPal account. For that click the **Buy as a guest** button. In the opened window enter your billing information.

![PayPal refill as guest](08-paypal-refill-as-guest.png)

Fill in all the required fields and press **Continue** button. After that enter your debit/credit card details in the appeared window.

![PayPal card details](09-paypal-card-details.png)

You'll get emails with information about the state of your account converting and refilling. Also such information will appear in the message at the dashboard.

{{%tip%}}**Note:** Using this method of payment you won't be able to use auto-refill option in the platform dashboard<a id="refilling"></a>.{{%/tip%}}


## Refilling

You can order recharge cards (One-Time Fee service plans) both from OBAS online store and the platform dashboard.

### Through Platform Dashboard

1\. If you need to replenish your account click **Balance > Refill balance**. State the sum using slider and click **Submit Payment**.

![refill ballance](10-refill-ballance.png)

2\. <u>If you use ***card*** as a payment method:</u>

Enter card details and click **Proceed**. Then enter the password for the full authentication.

![refill with card](11-refill-with-card.png)

{{%tip%}}**Tip:** If you have already refilled account with this card earlier you won't need to enter card details one more time. You just need to confirm refilling and that's all.{{%/tip%}}

3\. <u>If you use ***PayPal*** as a payment method:</u>

Log in to your PayPal account and complete the purchase.

![refill with PayPal](12-refill-with-paypal.png)

After replenishment you'll get emails with information about the state of your account refilling. Also such information will appear in the message at the dashboard.

4\. Also you can set auto-refill due to your demands. Click **Configure auto-refill** button in the drop-down menu.

![configure auto-refill button](13-configure-auto-refill-button.png)

In the opened tab specify the amount you want to put on your account and choose the frequency of refilling:

* *weekly* (every Monday)
* *monthly* (1st of each month)
* when *balance less than* the stated sum (up to your choice)

**Confirm** your choice.

![OBAS auto-refill](14-obas-auto-refill.png)

If you want to switch **Auto refill** off click the link to disable it.

![OBAS disable auto-refill](15-obas-disable-auto-refill.png)

5\. Using **Payment methods** button in the drop-down list you can choose your default payment method which will be used automatically while refilling.

6\. Click **View invoices** to open Odin Business Automation Control Panel with your Billing history which includes all financial documents issued for your Account (namely, Invoices, Orders, Payments, and Adjustments).

7\. Click **Billing history** to view the data about consuming the resources of your balance by the platform.

### Through OBAS Store

_**Prerequisites:** Your account need to be converted to billing._

List of *PaaS One-Time Fee* service plans is displayed in the main page of OBAS Online Store. You may choose and buy one of them.

![PaaS service plans in OBAS](16-paas-service-plans-in-obas.png)

1\. Choose the required **One-time fee item** and follow the steps of the wizard.

2\. State whether you are a new customer of OBAS or an existing one:

* ***I'm an Existing Customer*** - in this case you just need to enter your email address and password. Click **Sign In**.
![OBAS existing customer](17-obas-existing-customer.png)

* ***I'm a New Customer*** - if you don't have OBAS account yet, you have to perform trial-to-paid conversion process as listed in **Conversion** section.

3\. Your order has been prepared. Review the order details and click **Place Order** to proceed to the payment page.

![OBAS review and place order](18-obas-review-and-place-order.png)

4\. Select a payment method.

![OBAS payment method](19-obas-payment-method.png)

5\. Enter card details and click **Proceed** to complete the payment.

![OBAS card details](20-obas-card-details.png)


## What's next?

* [Billing System Overview](/billing-system/)
* [Upgrade & Refill Account](/upgrade-refill-account/)
* [Pricing Model Overview](/pricing-model/)