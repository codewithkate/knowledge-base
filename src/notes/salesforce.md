---
title: "No-Code Solutions for Embedding Tableau in Salesforce"
date: 2024-11-12
summary: "A tutorial on Tableau Lightning Web Components for desktop and mobile."
tags: ["notes", "UI/UX", "system design"]
---

## What are Salesforce Lightning Apps?

Salesforce is an app-based platform that has several no-Code solutions for adding web components to its interface. This works similar to web objects on a Tableau Dashboard.

There are two kinds of Salesforce apps: Classic and Lightning. Using apps in Lightning Experience allows your users to access content that is relevant to them through the **App Launcher**.

![[sf-applauncher.png]]

>[!Note] 
>Your profile determines which apps you can view and build. For this tutorial, you will need an admin access in Salesforce and Tableau Cloud.

## Create a New Lightning App 

Go to your Salesforce Site. Click the gear icon (⚙️) in the top right header to navigate to **Setup**. Use Quick Find to search for **App Manager** under Apps.

![[sf-appmanager.png]]

Create a New Lightning App. Give it a descriptive name for the team or department and add any custom branding. 

Keep default app options and utility items.  Unless you know the items you want to include as tabs in your app, then skip adding navigation items. Choose the user profiles that can access the app.

Finally, go to the app through the App Launcher. Continue reading  to customize this new app with navigation pages.

## Connect Tableau Cloud and Salesforce

>[!Note]
>Connections between Salesforce and Tableau Cloud Dev Sites have not worked in the past. It is recommended that you use active Tableau Cloud and Salesforce instances or Partner site credentials.

In Setup, search for **Trusted URLs** in the Quick Find search bar. We'll be adding your Tableau Cloud site as a **New Trusted URL**.

Enter an **API Name** and the **URL** for your cloud site. For example:

`https://some-location.online.tableau.com/#/site/your-site-name`

For this introduction, we will set the **CSP Context** to all and save.

Next, enter "Tableau Embedding" in Quick Find so we can setup token authentication for Tableau Pulse LWC.

Check the box to **Turn on SSO authentication with Tableau connected apps**.

You must use the same user identity for Salesforce as Tableau. For instance, you may use the same org email for Salesforce and Tableau, so you select it as your **Tableau User Identity field**. There are custome field options that are not covered here.

## Personalize App Home Page

We can create a new view to add to our home page. For this example, we will be embedding a Tableau Dashboard.

Go to Setup and search for **Lightning App Builder** from Quick Find. Cick New to create a Home Page. 

![[sf-appbuilder.png]] 

Search for Tableau in the Components Panel. If you want to embed a Tableau Dashboard or Worksheet then use **Tableau View**. We will be using **Tableau Pulse** to create a Mobile App in the next section.

Click and drag the Tableau View Component onto the main canvas. Enter a URL for the Tableau view and the Site ID for your organization's Tableau Site. Save the page.

Then, go to Activation and assign it as the home page for select apps.

If the activation was successful, then go back to your app. Click the pencil (✏️) icon to the right of the App name. Go to add more items and search for Home to add it to the navigation menu as a tab. You may need to repeat this step for other Desktop pages you create.

![[sf-tableaudashboard.png]]

Continue reading to learn how to make mobile-friendly pages.

## Create a Mobile App Page for Pulse

You can't access Desktop views from the Mobile App. You must create a phone layout. 

Within Lightning App Builder, create a new page. Name it Tableau Pulse with a One Region layout.

You should see a Phone layout selected above the canvas.

![[sf-phonelayout.png]]

Search for Tableau Pulse component and drag it onto the canvas.

Open Tableau Pulse and paste the full URL (including your site name).

Open Connected Apps in Tableau Cloud Settings. Find the Salesforce connection and Copy Site ID to paste into the App Setup.

Now, you can move onto adjusting the Activation settings.

1. Page Settings: Choose a display name, icon, and manage access.
2. Lightning Experience: Add the page to multiple Lightning Apps.
3. Mobile Navigation: Add and reorder pages available in the Salesforce App.

Save and get ready to preview the page in the Salesforce Mobile App.

## Preview Pulse in the Salesforce Mobile App

After downloading the Salesforce App, go to your device settings. You will need to **Allow Cross-Website Tracking**.

![[sf-devicesettings.png]]

Open the Salesforce App and go to the App Launcher on the Menu page. 

Find **Mobile Only** and you should be able to view your Tableau Pulse app from the navigation menu. 

![[sf-pulsemobile.png]]

## Wrap-up

Having followed these steps, you are all set to customize Salesforce Desktop and Mobile!

## Additional Resources

- [Learning Module | Lightning App Builder](https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder)
- [Learning Module | Lightning Experience Rollout](https://trailhead.salesforce.com/content/learn/modules/lex_migration_rollout)
- [Help Article | Extend Salesforce with Clicks, Not Code](https://help.salesforce.com/s/articleView?id=platform.extend_click_intro.htm&language=en_US&type=5)
- [Help Article | Configure Tableau and SSO](https://help.tableau.com/current/server/en-us/lwc_seamless_auth.htm)
- [Watch Demo | Build a Mobile App Page](https://admin.salesforce.com/blog/2019/build-a-mobile-app-page)
